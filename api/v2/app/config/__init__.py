from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Infilmation"

    class Config:
        env_file = '.env'

settings = Settings()
