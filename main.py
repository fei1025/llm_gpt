from fastapi import FastAPI
import uvicorn

from controller import document_controller


app = FastAPI()

app.include_router(document_controller.router)





@app.get("/demo")
async def demo():
    return "demo"


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
