from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from repositories.user_repo import UserRepository
from database import get_async_session
from schemas.user import UserCreate, UserRead, Token
from core.security import verify_password, create_access_token

router = APIRouter(
    prefix="/auth", 
    tags=["Auth"]
)

@router.post("/register", response_model=UserRead) # type: ignore
async def register(
    user_data: UserCreate, 
    db: AsyncSession = Depends(get_async_session)
):
    repo = UserRepository(db)

    existing_user = await repo.get_by_phone(user_data.phone)
    if existing_user:
        raise HTTPException(status_code=400, detail="Пользователь уже существует")

    return await repo.create(user_data)

@router.post("/login", response_model=Token)
async def login(
    user_data: UserCreate, 
    db: AsyncSession = Depends(get_async_session)
):
    repo = UserRepository(db)

    existing_user = await repo.get_by_phone(user_data.phone)
    if not existing_user or not verify_password(user_data.password, existing_user.hashed_password):
        raise HTTPException(status_code=401, detail="Неправильный логин или пароль")

    token = create_access_token(subject=str(existing_user.id))
    return {"access_token": token, "token_type": "bearer"}