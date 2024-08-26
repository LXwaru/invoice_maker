"""empty message

Revision ID: a4781557626e
Revises: f1e70ca0247a
Create Date: 2024-08-23 22:41:59.208696

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a4781557626e'
down_revision: Union[str, None] = 'f1e70ca0247a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
