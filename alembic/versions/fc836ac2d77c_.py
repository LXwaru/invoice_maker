"""empty message

Revision ID: fc836ac2d77c
Revises: 663bd7a7ea02
Create Date: 2024-08-26 15:04:42.344502

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fc836ac2d77c'
down_revision: Union[str, None] = '663bd7a7ea02'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
