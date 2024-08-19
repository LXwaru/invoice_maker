"""empty message

Revision ID: da79ceb4bdb9
Revises: d88a06ab8b03
Create Date: 2024-08-17 14:43:44.050666

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'da79ceb4bdb9'
down_revision: Union[str, None] = 'd88a06ab8b03'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
