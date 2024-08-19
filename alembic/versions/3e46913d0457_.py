"""empty message

Revision ID: 3e46913d0457
Revises: bad2e758f90c
Create Date: 2024-08-18 20:49:18.465901

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3e46913d0457'
down_revision: Union[str, None] = 'bad2e758f90c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
