from fastapi import APIRouter, Request, Response, UploadFile, File, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from . import crud

from api.tea.schemas import Product, ProductCreate
from core.models import db_config

router = APIRouter()


@router.post("/")
async def create_tea(product: ProductCreate, session: AsyncSession = Depends(db_config.get_session),
                     ):

    content = await crud.create_tea(session=session, product=product)
    return content
