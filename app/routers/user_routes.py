from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..schemas.user import UserCreate, UserInDB
from ..db.database import get_db
from dependency_injector.wiring import inject, Provide
from ..containers import Container

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserInDB)
@inject
async def create_user(
    user: UserCreate,
    db: AsyncSession = Depends(Provide[Container.db_session_provider])
):
    # 这里暂时返回模拟数据，后续可添加真实数据库操作
    return UserInDB(
        id=1,
        email=user.email,
        username=user.username,
        is_active=True
    )

@router.get("/{user_id}", response_model=UserInDB)
@inject
async def read_user(
    user_id: int,
    db: AsyncSession = Depends(Provide[Container.db_session_provider])
):
    return UserInDB(
        id=user_id,
        email="example@example.com",
        username="demo_user",
        is_active=True
    )