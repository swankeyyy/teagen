from fastapi import UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload, joinedload
from api.tea.schemas import ProductCreate, Product, TeaCountryList
from core.models import Tea, TeaType, TeaCountry


async def create_tea(session: AsyncSession, product: ProductCreate) -> Tea:
    item = Tea(**product.model_dump())
    session.add(item)
    await session.commit()
    await session.refresh(item)
    return item


async def load_tea_image(session: AsyncSession, tea_id: int, image: UploadFile) -> bool:
    stmt = select(Tea).where(tea_id == Tea.id)
    item = await session.scalar(stmt)
    if item:
        path = './media/'
        file_name = path + str(tea_id) + image.filename
        with open(file_name, 'wb+') as f:
            f.write(image.file.read())
            f.close()
        item.image = file_name[1:]
        await session.commit()
        await session.refresh(item)
        return True
    return False


async def get_tea_by_id(tea_id: int, session: AsyncSession) -> Tea | bool:
    stmt = select(Tea).where(tea_id == Tea.id).options(selectinload(Tea.tea_type), selectinload(Tea.tea_country))
    item = await session.scalar(stmt)
    if item:
        return item
    return False


async def get_all_teas(session: AsyncSession) -> list[Tea] | bool:
    stmt = select(Tea).options(selectinload(Tea.tea_type), selectinload(Tea.tea_country))
    items = await session.scalars(stmt)
    if items:
        return list(items)
    return False


async def get_all_tea_types(session: AsyncSession) -> list[TeaType] | bool:
    stmt = select(TeaType).options(joinedload(TeaType.teas))
    items = await session.execute(stmt)
    items = items.scalars().unique().all()
    if items:
        return list(items)
    return False


async def get_all_tea_countries(session: AsyncSession) -> list[TeaCountry] | bool:
    stmt = select(TeaCountry).options(joinedload(TeaCountry.teas))
    items = await session.execute(stmt)
    items = items.scalars().unique().all()
    if items:
        return list(items)
    return False

