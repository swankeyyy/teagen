from typing import Annotated
from fastapi.exceptions import HTTPException
from fastapi import APIRouter, Request, Response, UploadFile, File, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from . import crud
from api.tea.schemas import Product, ProductCreate, TypeList, TeaCountryList
from core.models import db_config

router = APIRouter()


@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED, summary="Post new tea")
async def create_tea_view(product: ProductCreate,
                          session: AsyncSession = Depends(db_config.get_session)):
    """Create a new tea with required parameters, upload image by created tea by another endpoint"""
    result = await crud.create_tea(session=session, product=product)
    return result


@router.post("/add_image/{tea_id}", summary="Upload image for tea by ID")
async def add_tea_image_view(tea_id: int, image: UploadFile,
                             session: AsyncSession = Depends(db_config.get_session)) -> Response:
    """Uploat image for existed tea by id"""
    result = await crud.load_tea_image(session=session, image=image, tea_id=tea_id)
    if result:
        return Response(status_code=201)
    raise HTTPException(500, detail='wrong id')


@router.get("/", response_model=list[Product], status_code=status.HTTP_200_OK, summary="Get list of items", )
async def get_all_teas_view(session: AsyncSession = Depends(db_config.get_session)):
    """returns list of all teas"""
    result = await crud.get_all_teas(session=session)
    if result:
        return result
    raise HTTPException(status_code=404, detail='Teas not found, at first create it')


@router.get("/types", response_model=list[TypeList], summary="Get list of categories",
            status_code=status.HTTP_200_OK)
async def get_all_tea_types_view(session: AsyncSession = Depends(db_config.get_session)):
    """return all tea categories with their list of teas"""
    result = await crud.get_all_tea_types(session=session)
    if result:
        return result
    raise HTTPException(status_code=404, detail='Categories not found, at first create it')


@router.get("/countries", response_model=list[TeaCountryList], status_code=status.HTTP_200_OK,
            summary="Get list of all Tea Countries")
async def get_all_tea_countries_view(session: AsyncSession = Depends(db_config.get_session)):
    result = await crud.get_all_tea_countries(session=session)
    if result:
        return result
    raise HTTPException(status_code=404, detail='Countries not found, at first create it')


@router.get("/{tea_id}", response_model=Product, status_code=status.HTTP_200_OK, summary="Get Tea by ID")
async def get_tea_by_id_view(tea_id: int, session: AsyncSession = Depends(db_config.get_session)):
    """get id and return description of tea by id"""

    result = await crud.get_tea_by_id(session=session, tea_id=tea_id)
    if result:
        return result
    raise HTTPException(status_code=404, detail='wrong ID')
