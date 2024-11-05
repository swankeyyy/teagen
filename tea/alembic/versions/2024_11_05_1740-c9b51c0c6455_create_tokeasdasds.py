"""Create tokeasdasds

Revision ID: c9b51c0c6455
Revises: df3a63579888
Create Date: 2024-11-05 17:40:59.842638

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c9b51c0c6455'
down_revision: Union[str, None] = 'df3a63579888'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('uq_accesstoken_id', 'accesstoken', type_='unique')
    op.drop_column('accesstoken', 'id')
    op.drop_constraint('uq_tea_id', 'tea', type_='unique')
    op.drop_constraint('uq_tea_country_id', 'tea_country', type_='unique')
    op.drop_constraint('uq_tea_type_id', 'tea_type', type_='unique')
    op.drop_constraint('uq_user_id', 'user', type_='unique')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('uq_user_id', 'user', ['id'])
    op.create_unique_constraint('uq_tea_type_id', 'tea_type', ['id'])
    op.create_unique_constraint('uq_tea_country_id', 'tea_country', ['id'])
    op.create_unique_constraint('uq_tea_id', 'tea', ['id'])
    op.add_column('accesstoken', sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_unique_constraint('uq_accesstoken_id', 'accesstoken', ['id'])
    # ### end Alembic commands ###
