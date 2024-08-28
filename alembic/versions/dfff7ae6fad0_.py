"""empty message

Revision ID: dfff7ae6fad0
Revises: 472bfcc03388
Create Date: 2024-08-26 15:31:41.848035

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dfff7ae6fad0'
down_revision: Union[str, None] = '472bfcc03388'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
