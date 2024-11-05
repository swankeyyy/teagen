from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import MetaData

naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
class Base(DeclarativeBase):
    __abstract__ = True
    # id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    metadata = MetaData(
        naming_convention=naming_convention,
    )



