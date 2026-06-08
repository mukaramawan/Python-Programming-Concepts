from fastapi import APIRouter

router = APIRouter()

@router.get("/login")
async def auth():
    return {"message": "authenticated!"}