"""empty message

Revision ID: e2951c84ca41
Revises: fda4934a04b3
Create Date: 2024-08-16 23:03:09.053824

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e2951c84ca41'
down_revision: Union[str, None] = 'fda4934a04b3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
