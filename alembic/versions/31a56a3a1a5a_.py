"""empty message

Revision ID: 31a56a3a1a5a
Revises: d908c5bd90cc
Create Date: 2024-08-26 15:26:42.577566

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '31a56a3a1a5a'
down_revision: Union[str, None] = 'd908c5bd90cc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
