from fastapi import Depends, HTTPException, Request
from dependencies.supabase_client import get_supabase_client
from services.user.user_service import UserService

class AuthService:
    """
    認証サービス
    """
    def __init__(self, 
                 supabase_client=Depends(get_supabase_client), 
                 user_service=Depends(UserService)):
        """
        初期化
        """
        self.client = supabase_client
        self.user_service = user_service

    def sign_up(self, email: str, password: str, name: str):
        """
        サインアップ処理 + ユーザーデータベース登録
        """
        # Supabase Authに登録
        try:
            result = self.client.auth.sign_up({"email": email, "password": password})
            print(f"01. signup success.")
        except Exception as e:
            print(f"01. Error signing up: {e}")
            raise Exception(f"Error signing up: {e}")

        # ユーザーIDを取得
        user_id = result.user.id if result.user else None
        print(f"02. get user_id: {user_id}")
        if not user_id:
            print(f"02. User ID not found in signup response: {result}")
            raise Exception("User ID not found in signup response.")
        
        # ユーザーデータベースに登録
        try:
            self.user_service.create_user(user_id, name, email)
            print(f"03. create user: {user_id}")
        except Exception as e:
            print(f"03. Error creating user: {e}")
            raise Exception(f"Error creating user: {e}")

        return {"message": "User created successfully", "data": result}

    def sign_in(self, email: str, password: str):
        """
        ログイン処理
        """
        try:
            result = self.client.auth.sign_in_with_password({"email": email, "password": password})
            print(f"01. sign_in result: {result}")
        except Exception as e:
            print(f"01. Error signing in: {e}")
            raise Exception(f"Error signing in: {e}")

        # ログイン成功
        access_token = result.session.access_token if result.session else None
        if not access_token:
            print(f"02. Access token not found in signin response: {result}")
            raise Exception("Access token not found in signin response.")

        return {"message": "Login successful", "access_token": access_token}
    
    def get_current_user(self, request: Request):
        """
        クッキーまたはヘッダからアクセストークンを取得し、ユーザー情報を検証
        """
        token = request.cookies.get("access_token")  # クッキーからアクセストークンを取得
        if not token:
            print(f"01. not token error.")
            raise Exception("Access token missing")

        # トークンを使ってユーザー情報を取得
        try:
            print(f"02. get user. token: {token}")
            user = self.client.auth.get_user(token)
            if not user:
                print(f"02. invalid token error.")
                raise Exception("Invalid credentials")
            return user
        except Exception as e:
            print(f"03. invalid token error. {e}")
            raise Exception("Invalid credentials")
