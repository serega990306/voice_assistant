from pydantic import Field
from pydantic_settings import BaseSettings

env_file = ".env.example"


class Settings(BaseSettings):
    queue: str = Field(env="QUEUE")
    host: str = Field(env="HOST")
    port: str = Field(env="PORT")
    name: str = Field(env="NAME")
    password: str = Field(env="PASSWORD")

    class Config:
        env_file = env_file


settings = Settings()