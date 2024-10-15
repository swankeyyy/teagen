from fastapi import FastAPI
import uvicorn
from api import router as api_router
from contextlib import asynccontextmanager
from core.models import db_config


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await db_config.dispose()


main_app = FastAPI(lifespan=lifespan)

main_app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("main:main_app",

                reload=True)
