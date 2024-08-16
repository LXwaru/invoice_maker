"""empty message

Revision ID: 56c0f061f708
Revises: f6af41c40faf
Create Date: 2024-08-15 22:27:41.454291

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '56c0f061f708'
down_revision: Union[str, None] = 'f6af41c40faf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
