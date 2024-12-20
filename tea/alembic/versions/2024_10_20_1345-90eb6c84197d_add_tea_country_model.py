"""add Tea Country model

Revision ID: 90eb6c84197d
Revises: 01f0ed020484
Create Date: 2024-10-20 13:45:45.997710

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '90eb6c84197d'
down_revision: Union[str, None] = '01f0ed020484'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tea_country',
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.add_column('tea', sa.Column('tea_country_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'tea', 'tea_country', ['tea_country_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tea', type_='foreignkey')
    op.drop_column('tea', 'tea_country_id')
    op.drop_table('tea_country')
    # ### end Alembic commands ###
