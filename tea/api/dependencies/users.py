from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import User
from core.models.db_config import db_config


async def get_users_db(session: AsyncSession = Depends(db_config.get_session)):
    yield User.get_db(session=session)
