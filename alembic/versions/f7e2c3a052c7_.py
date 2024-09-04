"""empty message

Revision ID: f7e2c3a052c7
Revises: 8a2561861a71
Create Date: 2024-09-04 13:51:00.925607

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f7e2c3a052c7'
down_revision: Union[str, None] = '8a2561861a71'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
