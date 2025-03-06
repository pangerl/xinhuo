from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserCreate, UserInDB
import logging
# from app.db.database import get_db
from dependency_injector.wiring import inject, Provide
from app.containers import Container
from app.db import crud

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserInDB)
@inject
async def create_user(
    user: UserCreate,
    db: AsyncSession = Depends(Provide[Container.db_session_provider])
):
    try:
        # 调用数据库操作函数创建用户
        new_user = await crud.create_user(db, user)
        return new_user
    except Exception as e:
        logging.error("创建用户时发生错误", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{user_id}", response_model=UserInDB)
@inject
async def read_user(
    user_id: int,
    db: AsyncSession = Depends(Provide[Container.db_session_provider])
):
    try:
        # 调用数据库操作函数查询用户
        user = await crud.get_user(db, user_id)
        if user is None:
            # 若用户不存在，返回 404 错误
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except Exception as e:
        # 处理数据库操作异常
        raise HTTPException(status_code=500, detail=str(e))
