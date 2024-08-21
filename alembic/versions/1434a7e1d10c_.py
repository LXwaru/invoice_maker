"""empty message

Revision ID: 1434a7e1d10c
Revises: e1f86cb469f4
Create Date: 2024-08-21 16:05:26.127687

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1434a7e1d10c'
down_revision: Union[str, None] = 'e1f86cb469f4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
