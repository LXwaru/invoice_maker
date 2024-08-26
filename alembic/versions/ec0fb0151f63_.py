"""empty message

Revision ID: ec0fb0151f63
Revises: 22c58fb10d65
Create Date: 2024-08-25 13:08:24.785743

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ec0fb0151f63'
down_revision: Union[str, None] = '22c58fb10d65'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
