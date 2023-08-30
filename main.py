import time

import aioredis

from fastapi import  Request, FastAPI

import uvicorn
from functools import lru_cache

from controller import document_controller
import config


app = FastAPI()

app.include_router(document_controller.router)

@lru_cache()
def get_settings():
   return config.Settings()




@app.get("/demo")
async def demo(request: Request):
    settings = get_settings()
    redis:aioredis =  request.state.redis
    await redis.set("key111", "string-value22222222222")
    print(settings.openai_api_key)
    return "demo"
# 整合redis
# https://blog.csdn.net/RoninYang/article/details/121128050
# redis 文档
# https://aioredis.readthedocs.io/en/latest/getting-started/
# 矢量redis

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    print(request.headers["token"])
    request.state.redis=app.state.redis
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.on_event("startup")
async def startup_event():
    settings = get_settings()
    app.state.redis: aioredis = await aioredis.from_url(settings.redis_url)
    print("redis连接成功")

@app.on_event("shutdown")
async def shutdown_event():
    await app.state.redis.close()





if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
