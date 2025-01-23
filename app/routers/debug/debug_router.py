from fastapi import APIRouter

# debug.pyのルーターを作成
router = APIRouter()

# debug_endpoint関数を作成
@router.get("/")
async def debug_endpoint():
    return {"message": "Debug data"}
