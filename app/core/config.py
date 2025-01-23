from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    設定クラス
    """
    SUPABASE_URL: str
    SUPABASE_ANON_KEY: str
    PORT: int

    class Config:
        """
        設定クラスの設定
        """
        env_file = ".env"

settings = Settings()
