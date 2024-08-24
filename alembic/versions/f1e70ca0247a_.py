"""empty message

Revision ID: f1e70ca0247a
Revises: 1434a7e1d10c
Create Date: 2024-08-23 21:44:53.940655

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f1e70ca0247a'
down_revision: Union[str, None] = '1434a7e1d10c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
