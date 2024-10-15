from sqlalchemy.ext.asyncio import AsyncSession
from api.tea.schemas import ProductCreate, Product
from core.models import Tea


async def create_tea(session: AsyncSession, product: ProductCreate) -> Tea:
    product = Tea(**product.model_dump())
    session.add(product)
    await session.commit()
    await session.refresh(product)
    return product
