"""empty message

Revision ID: 5cd8da948ee6
Revises: 0e1fbb840f60
Create Date: 2024-09-05 15:14:33.951795

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5cd8da948ee6'
down_revision: Union[str, None] = '0e1fbb840f60'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
