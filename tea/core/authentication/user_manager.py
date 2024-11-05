from typing import Optional
from core.types.user_id import UserIdType
from fastapi import Request
from fastapi_users import BaseUserManager, UUIDIDMixin

from core.models.user import User
from core.models.base import Base
SECRET = "hjgk123asd213hjghjgt8787678687tfghfjgfjgj"


class UserManager(Base, BaseUserManager[User, UserIdType]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


