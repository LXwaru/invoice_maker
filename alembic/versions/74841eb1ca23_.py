"""empty message

Revision ID: 74841eb1ca23
Revises: 3e46913d0457
Create Date: 2024-08-18 20:50:02.043105

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '74841eb1ca23'
down_revision: Union[str, None] = '3e46913d0457'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
