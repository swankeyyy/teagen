from fastapi import APIRouter
from core.types.user_id import UserIdType
from fastapi_users import FastAPIUsers
from api.dependencies.user_manager import get_user_manager
from core.models.user import User
from api.dependencies.backend import authentication_backend
from .schemas import UserRead, UserCreate, UserUpdate
fastapi_users = FastAPIUsers[User, UserIdType](
    get_user_manager,
    [authentication_backend],
)

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

# /login /logout
router.include_router(fastapi_users.get_auth_router(authentication_backend))

# /register
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),)

router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users")