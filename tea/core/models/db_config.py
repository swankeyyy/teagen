from sqlalchemy.ext.asyncio import (create_async_engine, AsyncEngine, AsyncSession,
                                    async_sessionmaker)

from tea.core import settings


class DBConfig:
    def __init__(self, url: str, echo: bool = False) -> None:
        self.engine: AsyncEngine = create_async_engine(url=url, echo=echo)
        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(bind=self.engine)

    async def dispose(self) -> None:
        """close database engine"""
        await self.engine.dispose()

    async def get_session(self) -> AsyncSession:
        async with self.session_factory() as session:
            yield session


db_config = DBConfig(settings.DB_URL, settings.DB_ECHO)
