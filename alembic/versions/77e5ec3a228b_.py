"""empty message

Revision ID: 77e5ec3a228b
Revises: 3bc22ca9d31e
Create Date: 2024-09-04 14:17:12.293698

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '77e5ec3a228b'
down_revision: Union[str, None] = '3bc22ca9d31e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
