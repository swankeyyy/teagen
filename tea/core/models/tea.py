from core.models import Base
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped


class Tea(Base):
    __tablename__ = 'tea'

    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str] = mapped_column(String(200), )
    cook_time: Mapped[float] = mapped_column(default=0.0, )
    price: Mapped[str] = mapped_column(String(4))
    image: Mapped[str] = mapped_column(String(200), nullable=True)