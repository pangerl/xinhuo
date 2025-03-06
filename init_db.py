from alembic import command
from alembic.config import Config
from app.models.user import Base
from app.db.database import async_engine


async def init_db():
    """初始化数据库: 创建表"""
    print("Creating database tables...")
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Database tables created successfully.")


def revision_db():
    """使用 Alembic 生成迁移脚本"""
    print("Generating database migration...")
    alembic_cfg = Config("alembic.ini")
    command.revision(alembic_cfg, autogenerate=True)
    print("Database migration generated successfully.")


def upgrade_db():
    """使用 Alembic 进行数据库迁移"""
    print("Upgrading database schema...")
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")
    print("Database schema upgraded successfully.")


def downgrade_db():
    """回退数据库迁移"""
    print("Downgrading database schema...")
    alembic_cfg = Config("alembic.ini")
    command.downgrade(alembic_cfg, "-1")
    print("Database schema downgraded successfully.")


if __name__ == "__main__":
    import sys
    import asyncio

    if len(sys.argv) < 2:
        print("Usage: python init_db.py [init|upgrade|downgrade]")
        sys.exit(1)

    action = sys.argv[1].lower()
    if action == "init":
        asyncio.run(init_db())
    elif action == "revision":
        revision_db()
    elif action == "upgrade":
        upgrade_db()
    elif action == "downgrade":
        downgrade_db()
    else:
        print("Invalid command. Use: init, upgrade, or downgrade")