"""empty message

Revision ID: 9a1a8bb57f06
Revises: e83b7a796376
Create Date: 2024-09-05 16:11:08.487883

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9a1a8bb57f06'
down_revision: Union[str, None] = 'e83b7a796376'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
