"""empty message

Revision ID: 6e11ffd3becc
Revises: a75174f0dee2
Create Date: 2024-08-15 22:31:05.194408

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6e11ffd3becc'
down_revision: Union[str, None] = 'a75174f0dee2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
