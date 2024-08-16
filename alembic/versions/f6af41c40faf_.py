"""empty message

Revision ID: f6af41c40faf
Revises: d8c9dbd38d1e
Create Date: 2024-08-15 22:26:24.240157

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f6af41c40faf'
down_revision: Union[str, None] = 'd8c9dbd38d1e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
