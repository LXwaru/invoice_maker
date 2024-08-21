"""empty message

Revision ID: 6922bc6158df
Revises: a5ffa6f99e06
Create Date: 2024-08-21 14:35:45.781292

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6922bc6158df'
down_revision: Union[str, None] = 'a5ffa6f99e06'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
