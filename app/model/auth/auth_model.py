from pydantic import BaseModel

class SignUpRequest(BaseModel):
    """
    サインアップリクエスト
    """
    name: str
    email: str
    password: str

class SignUpResponse(BaseModel):
    """
    サインアップレスポンス
    """
    message: str
    
class LoginRequest(BaseModel):
    """
    ログインリクエスト
    """
    email: str
    password: str

class LoginResponse(BaseModel):
    """
    ログインレスポンス
    """
    message: str