from fastapi import Depends
from dependencies.supabase_client import get_supabase_client

class UserRepository:
    """
    ユーザーリポジトリ
    """
    def __init__(self, supabase_client=Depends(get_supabase_client)):
        """
        初期化
        """
        self.client = supabase_client

    def create_user(self, user_id: str, name: str, email: str):
        """
        新しいユーザーを user テーブルに追加
        """
        data = {
            "id": user_id,
            "name": name,
            "email": email,
        }
        
        response = self.client.table("user").insert(data).execute()
        if response.error:
            print(f"Error creating user: {response.error.message}")
            raise Exception(f"Error creating user: {response.error.message}")
        return response

def get_user_repository():
    return UserRepository()
