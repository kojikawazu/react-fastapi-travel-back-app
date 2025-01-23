from fastapi import FastAPI
from routers.debug import debug_router
from routers.auth import auth_router

# FastAPIのインスタンスを作成
app = FastAPI()

# ルーターの登録
app.include_router(debug_router.router, prefix="/debug", tags=["Debug"])
app.include_router(auth_router.router, prefix="/auth", tags=["Auth"])
