from fastapi import Depends
from fastapi_users.authentication.strategy.db import AccessTokenDatabase, DatabaseStrategy

from api.dependencies.access_tokens import get_access_token_db
from core.models.access_token import AccessToken


def get_database_strategy(
        access_token_db: AccessTokenDatabase[AccessToken] = Depends(get_access_token_db),
) -> DatabaseStrategy:
    return DatabaseStrategy(database=access_token_db, lifetime_seconds=3600)
