from pydantic_settings import BaseSettings


class ServerSettings(BaseSettings):
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    MODE: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = ServerSettings()  # type: ignore
