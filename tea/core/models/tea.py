from core.models import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import List


class Tea(Base):
    __tablename__ = 'tea'

    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str] = mapped_column(String(200), )
    cook_time: Mapped[float] = mapped_column(default=0.0, )
    price: Mapped[str] = mapped_column(String(4))
    image: Mapped[str] = mapped_column(String(200), nullable=True)
    tea_type_id: Mapped[int] = mapped_column(ForeignKey('tea_type.id'))
    tea_type: Mapped["TeaType"] = relationship(back_populates="teas")
    tea_country_id: Mapped[int] = mapped_column(ForeignKey('tea_country.id'), nullable=True)
    tea_country: Mapped["TeaCountry"] = relationship(back_populates="teas")

    def __repr__(self):
        return f"<Tea({self.name}, {self.id})>"


class TeaType(Base):
    __tablename__ = 'tea_type'

    name: Mapped[str] = mapped_column()
    teas: Mapped[List["Tea"]] = relationship(back_populates="tea_type", cascade="all, delete-orphan", lazy="select")

    def __repr__(self):
        return f"<Type({self.name}, {self.id})>"


class TeaCountry(Base):
    __tablename__ = 'tea_country'
    name: Mapped[str] = mapped_column(String(length=30), unique=True)
    description: Mapped[str] = mapped_column(String(length=200), )
    teas: Mapped[List["Tea"]] = relationship(back_populates="tea_country", cascade="all, delete-orphan",
                                             lazy="select")

    def __repr__(self):
        return f"<Country({self.name}, {self.id})>"