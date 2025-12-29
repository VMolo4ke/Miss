from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from repositories.user_repo import UserRepository
from database import get_async_session
from schemas.user import UserCreate, UserRead

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
