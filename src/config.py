from pydantic import Field
from pydantic_settings import BaseSettings

env_file = ".env"


class Settings(BaseSettings):
    openai_api_key: str = Field(env="OPENAI_API_KEY")

    class Config:
        env_file = env_file


settings = Settings()
