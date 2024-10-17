from fastapi import UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from api.tea.schemas import ProductCreate, Product
from core.models import Tea


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
    stmt = select(Tea).where(tea_id == Tea.id)
    item = await session.scalar(stmt)
    if item:
        return item
    return False
