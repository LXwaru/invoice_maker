"""empty message

Revision ID: 0764ce9b728d
Revises: 5fc5cc5ab268
Create Date: 2024-09-04 15:17:57.575632

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0764ce9b728d'
down_revision: Union[str, None] = '5fc5cc5ab268'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
