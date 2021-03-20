from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Infilmation"
    sqlalchemy_database_uri: str

    class Config:
        env_file = '.env'

settings = Settings()
