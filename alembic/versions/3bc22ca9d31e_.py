"""empty message

Revision ID: 3bc22ca9d31e
Revises: f7e2c3a052c7
Create Date: 2024-09-04 13:52:21.529271

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3bc22ca9d31e'
down_revision: Union[str, None] = 'f7e2c3a052c7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
