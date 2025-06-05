from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_name: str = 'pomodoro_db'