from fastapi import Depends
from repositories.user.user_repository import get_user_repository

class UserService:
    """
    ユーザーサービス
    """
    def __init__(self, user_repository=Depends(get_user_repository)):
        """
        初期化
        """
        self.user_repository = user_repository

    def create_user(self, user_id: str, name: str, email: str):
        """
        新しいユーザーを user テーブルに追加
        """
        try:
            response = self.user_repository.create_user(user_id, name, email)
            return response
        except Exception as e:
            print(f"Error creating user: {e}")
            raise e

def get_user_service():
    return UserService()
