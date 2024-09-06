"""empty message

Revision ID: c62fb92b3579
Revises: bc2316763448
Create Date: 2024-09-05 15:36:59.949824

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c62fb92b3579'
down_revision: Union[str, None] = 'bc2316763448'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
