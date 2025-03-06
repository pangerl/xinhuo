from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserCreate
from app.models.user import User  # 假设存在 User 模型
from sqlalchemy import select


# 创建用户
async def create_user(db: AsyncSession, user: UserCreate):
    # 用户名重复检查
    existing_user = await get_user_by_username(db, user.username)
    if existing_user:
        raise ValueError("Username already registered")
    db_user = User(**user.dict())
    if not hasattr(db_user, 'is_active'):
        db_user.is_active = True
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


# 查询用户
async def get_user(db: AsyncSession, user_id: int):
    return await db.get(User, user_id)


async def get_user_by_username(db: AsyncSession, username: str):
    result = await db.execute(select(User).where(User.username == username))
    return result.scalars().first()

