from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    openai_api_key:str
    redis_vector_url:str
    redis_url:str
    class Config:
        env_file = ".env"
