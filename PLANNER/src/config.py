from pydantic import ConfigDict
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # 환경변수에 비식별화 하기
    DATABASE_URL: str | None = None
    
    model_config = ConfigDict(
        env_file = '.env',
    ) 
    
settings = Settings()