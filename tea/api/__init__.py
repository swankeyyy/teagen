from fastapi import APIRouter
from .tea.views import router as tea_router
from .users.views import router as users_router
router = APIRouter(prefix="/api")
router.include_router(tea_router, prefix="/tea", tags=["teas"])
router.include_router(users_router)