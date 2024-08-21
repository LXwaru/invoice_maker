"""empty message

Revision ID: e1f86cb469f4
Revises: 6922bc6158df
Create Date: 2024-08-21 16:05:07.711889

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e1f86cb469f4'
down_revision: Union[str, None] = '6922bc6158df'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
