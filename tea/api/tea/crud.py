from fastapi import UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from api.tea.schemas import ProductCreate, Product
from core.models import Tea


async def create_tea(session: AsyncSession, product: ProductCreate) -> Tea:
    product = Tea(**product.model_dump())
    session.add(product)
    await session.commit()
    await session.refresh(product)
    return product


async def load_tea_image(session: AsyncSession, tea_id: int, image: UploadFile) -> bool:
    stmt = select(Tea).where(tea_id == Tea.id)
    item = await session.scalar(stmt)
    if item:
        path = './media/'
        file_name = path + str(tea_id) + image.filename
        with open(file_name, 'wb+') as f:
            f.write(image.file.read())
            f.close()
        item.image = file_name
        await session.commit()
        await session.refresh(item)
        print(item.image)
        return True
    return False
