"""empty message

Revision ID: e5afb5d60304
Revises: 74841eb1ca23
Create Date: 2024-08-18 22:41:59.495991

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e5afb5d60304'
down_revision: Union[str, None] = '74841eb1ca23'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
