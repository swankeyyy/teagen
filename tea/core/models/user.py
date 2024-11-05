from .base import Base
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from core.types.user_id import UserIdType
from .mixins.id_int_pk import IdIntPkMixin


class User(Base, IdIntPkMixin, SQLAlchemyBaseUserTable[UserIdType]):

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, cls)
