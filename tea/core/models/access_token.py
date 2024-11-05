from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from fastapi_users_db_sqlalchemy.access_token import (

    SQLAlchemyBaseAccessTokenTable,
)
from sqlalchemy.ext.asyncio import AsyncSession
from core.types.user_id import UserIdType


class AccessToken(SQLAlchemyBaseAccessTokenTable[UserIdType], Base):
    user_id: Mapped[UserIdType] = mapped_column(
        Integer, ForeignKey("user.id", ondelete="cascade"), nullable=False
    )

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, cls)


