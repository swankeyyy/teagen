from typing import Annotated

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
async def add_tea_image_view(tea_id: int, image: UploadFile):
    print(image.filename)
    path = './media/'
    file_name = path + str(tea_id) + image.filename
    with open(file_name, 'wb+') as f:
        f.write(image.file.read())
        f.close()

    return file_name
