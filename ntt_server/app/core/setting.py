from pydantic_settings import BaseSettings


class ServerSettings(BaseSettings):
    SECRET_KEY: str
    DATABASE_URL: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    LOG_FILE: str
    MODE: str
    HOST: str
    PORT: int

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = ServerSettings()  # type: ignore
