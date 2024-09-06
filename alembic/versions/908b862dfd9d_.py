"""empty message

Revision ID: 908b862dfd9d
Revises: 1604d53126cf
Create Date: 2024-09-05 16:18:30.897522

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '908b862dfd9d'
down_revision: Union[str, None] = '1604d53126cf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
