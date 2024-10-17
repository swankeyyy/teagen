from fastapi import FastAPI
import uvicorn
from starlette.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from api import router as api_router
from contextlib import asynccontextmanager
from core.models import db_config


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await db_config.dispose()


main_app = FastAPI(lifespan=lifespan)


@main_app.get("/media/{img}", tags=["media"], summary="Response Image by path")
async def media_view(img: str) -> FileResponse:
    """response image by path from item db"""
    print(img)
    return FileResponse(f'media/{img}', status_code=200)

main_app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("main:main_app",

                reload=True)
