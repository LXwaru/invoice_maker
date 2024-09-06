"""empty message

Revision ID: c9cd6a65cc75
Revises: c9e4f00a7766
Create Date: 2024-09-05 16:26:50.912561

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c9cd6a65cc75'
down_revision: Union[str, None] = 'c9e4f00a7766'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
