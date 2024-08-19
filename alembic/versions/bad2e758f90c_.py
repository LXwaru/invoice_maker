"""empty message

Revision ID: bad2e758f90c
Revises: da79ceb4bdb9
Create Date: 2024-08-17 14:45:38.674542

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bad2e758f90c'
down_revision: Union[str, None] = 'da79ceb4bdb9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
