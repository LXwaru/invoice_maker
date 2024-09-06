"""empty message

Revision ID: 3bb80fef9f74
Revises: 5d697f23258e
Create Date: 2024-09-05 15:43:20.549439

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3bb80fef9f74'
down_revision: Union[str, None] = '5d697f23258e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
