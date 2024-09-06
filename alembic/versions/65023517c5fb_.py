"""empty message

Revision ID: 65023517c5fb
Revises: 3bb80fef9f74
Create Date: 2024-09-05 15:49:20.925649

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '65023517c5fb'
down_revision: Union[str, None] = '3bb80fef9f74'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
