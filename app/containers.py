from dependency_injector import containers, providers
from app.db.database import AsyncSessionLocal, async_engine
import logging
from sqlalchemy.exc import SQLAlchemyError
import os
from logging.handlers import RotatingFileHandler


class Container(containers.DeclarativeContainer):
    db_session_provider = providers.Factory(
        AsyncSessionLocal
    )


async def init_container():
    # 配置日志系统
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        handlers=[
            RotatingFileHandler('logs/app.log', maxBytes=1024*1024*5, backupCount=3),
            logging.StreamHandler()
        ]
    )
    
    # 创建日志目录
    os.makedirs('logs', exist_ok=True)
    
    container = Container()
    try:
        await async_engine.dispose()
    except SQLAlchemyError as e:
        logging.error(f"SQLAlchemy error disposing engine: {e}", exc_info=True)
    except Exception as e:
        logging.error(f"Unexpected error during engine disposal: {e}", exc_info=True)
    return container
