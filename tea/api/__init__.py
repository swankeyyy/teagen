from fastapi import APIRouter
from .tea.views import router as tea_router
router = APIRouter(prefix="/api", tags=["main"])
router.include_router(tea_router, prefix="/tea")