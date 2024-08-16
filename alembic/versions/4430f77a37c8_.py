"""empty message

Revision ID: 4430f77a37c8
Revises: 30374b0483e4
Create Date: 2024-08-16 14:07:55.900258

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4430f77a37c8'
down_revision: Union[str, None] = '30374b0483e4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
