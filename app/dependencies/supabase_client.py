from supabase import create_client
from core.config import settings

class SupabaseClient:
    """
    Supabaseクライアント
    """
    def __init__(self):
        """
        Supabaseクライアントの初期化
        """
        self.client = create_client(settings.SUPABASE_URL, settings.SUPABASE_ANON_KEY)

    def get_client(self):
        return self.client

# DI用ファクトリ
def get_supabase_client():
    """
    Supabaseクライアントの取得
    """
    return SupabaseClient().get_client()
