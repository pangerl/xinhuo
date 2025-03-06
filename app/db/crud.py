from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserCreate
from app.models.user import User  # 假设存在 User 模型


# 创建用户
async def create_user(db: AsyncSession, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


# 查询用户
async def get_user(db: AsyncSession, user_id: int):
    return await db.get(User, user_id)