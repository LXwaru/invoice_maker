"""empty message

Revision ID: e83b7a796376
Revises: 20c73646a46d
Create Date: 2024-09-05 16:06:04.926060

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e83b7a796376'
down_revision: Union[str, None] = '20c73646a46d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
