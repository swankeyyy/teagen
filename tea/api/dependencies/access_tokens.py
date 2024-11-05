from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import AccessToken
from core.models.db_config import db_config


async def get_access_token_db(
        session: AsyncSession = Depends(db_config.get_db_session),
):
    yield AccessToken.get_db(session=session)
