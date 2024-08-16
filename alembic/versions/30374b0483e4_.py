"""empty message

Revision ID: 30374b0483e4
Revises: 6e11ffd3becc
Create Date: 2024-08-15 22:33:28.938634

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '30374b0483e4'
down_revision: Union[str, None] = '6e11ffd3becc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
