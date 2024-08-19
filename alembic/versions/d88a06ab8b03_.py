"""empty message

Revision ID: d88a06ab8b03
Revises: e2951c84ca41
Create Date: 2024-08-17 14:36:53.130888

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd88a06ab8b03'
down_revision: Union[str, None] = 'e2951c84ca41'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
