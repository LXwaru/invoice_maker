"""empty message

Revision ID: d908c5bd90cc
Revises: fc836ac2d77c
Create Date: 2024-08-26 15:19:58.384619

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd908c5bd90cc'
down_revision: Union[str, None] = 'fc836ac2d77c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
