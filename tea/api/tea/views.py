from typing import Annotated
from fastapi.exceptions import HTTPException
from fastapi import APIRouter, Request, Response, UploadFile, File, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from . import crud

from api.tea.schemas import Product, ProductCreate
from core.models import db_config

router = APIRouter()


@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_tea_view(product: ProductCreate,
                          session: AsyncSession = Depends(db_config.get_session)):
    content = await crud.create_tea(session=session, product=product)
    return content


@router.post("/add_image/{tea_id}")
async def add_tea_image_view(tea_id: int, image: UploadFile, session: AsyncSession = Depends(db_config.get_session)) -> Response:
    result = await crud.load_tea_image(session=session, image=image, tea_id=tea_id)
    if result:
        return Response(status_code=201)
    raise HTTPException(500, detail='wrong id')