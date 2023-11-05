from dataclasses import dataclass
from dotenv import find_dotenv, dotenv_values


@dataclass
class Settings:
    HOST: str
    PORT: int
    USERNAME: str
    PASSWORD: str


def get_settings() -> Settings:
    return Settings(**dotenv_values(find_dotenv()))
