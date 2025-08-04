from fastapi import APIRouter, Depends
from  ..core.dependencies import get_token_from_header

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
    dependencies=[Depends(get_token_from_header)],
    responses={403:{'description':"Not found"}}
)

@router.get("/signin")
async def sign_in():
    return {
        "username":"Priyanshu"
    }