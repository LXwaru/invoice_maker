"""empty message

Revision ID: 1604d53126cf
Revises: 9a1a8bb57f06
Create Date: 2024-09-05 16:13:30.569585

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1604d53126cf'
down_revision: Union[str, None] = '9a1a8bb57f06'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
