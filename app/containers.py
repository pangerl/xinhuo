from dependency_injector import containers, providers
from .db.database import AsyncSessionLocal, async_engine

class Container(containers.DeclarativeContainer):
    db_session_provider = providers.Resource(
        AsyncSessionLocal
    )

async def init_container():
    container = Container()
    await async_engine.dispose()
    return container