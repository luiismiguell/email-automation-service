import os

from dotenv import load_dotenv
from pydantic import BaseSettings, Field

load_dotenv()


class Settings(BaseSettings):
    EMAIL_USER: str = Field(..., env="EMAIL_USER")
    EMAIL_PASS: str = Field(..., env="EMAIL_PASS")
    SMTP_SERVER: str = Field("smtp.gmail.com", env="SMTP_SERVER")
    SMTP_PORT: int = Field(587, env="SMTP_PORT")

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
