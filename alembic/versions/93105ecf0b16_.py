"""empty message

Revision ID: 93105ecf0b16
Revises: 4430f77a37c8
Create Date: 2024-08-16 14:14:10.059860

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '93105ecf0b16'
down_revision: Union[str, None] = '4430f77a37c8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
