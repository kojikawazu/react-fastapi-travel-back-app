from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from services.auth.auth_service import AuthService
from model.auth.auth_model import SignUpRequest, SignUpResponse, LoginRequest, LoginResponse

# ルーターの生成
router = APIRouter()


@router.post("/signup", response_model=SignUpResponse)
async def signup(
    request: SignUpRequest,
    auth_service: AuthService = Depends(AuthService)
):
    """
    サインアップエンドポイント
    """
    try:
        auth_service.sign_up(request.email, request.password, request.name)
        return SignUpResponse(message="Signup successful")
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=400, detail="Invalid credentials")

@router.post("/login", response_model=LoginResponse)
async def login(
    request: LoginRequest,
    auth_service: AuthService = Depends(AuthService)
):
    """
    ログインエンドポイント
    """
    try:
        # サインイン処理
        result = auth_service.sign_in(request.email, request.password)
        
        # アクセストークンを取得
        print(f"02. access_token.")
        access_token = result.get("access_token")
        if not access_token:
            print(f"02. Access token not found.")
            raise HTTPException(status_code=400, detail="Access token not found.")
        
        # HTTPOnly cookieでアクセストークンをセット
        print(f"03. set cookie")
        response = JSONResponse({"message": "Login successful"})
        response.set_cookie("access_token", access_token, httponly=True, secure=False, samesite="Lax")
        
        print(f"04. login success.")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=401, detail="Invalid credentials")

@router.get("/protected")
async def protected_route(
    request: Request, 
    auth_service: AuthService = Depends(AuthService)
):
    """
    認証されたユーザーのみがアクセスできるエンドポイント
    """
    try:
        user = auth_service.get_current_user(request)
        return {"message": "Welcome, authenticated user!", "user": user}
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=401, detail="Invalid credentials")
