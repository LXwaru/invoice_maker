"""empty message

Revision ID: a75174f0dee2
Revises: 56c0f061f708
Create Date: 2024-08-15 22:29:38.654075

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a75174f0dee2'
down_revision: Union[str, None] = '56c0f061f708'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
