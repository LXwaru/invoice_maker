"""empty message

Revision ID: 472bfcc03388
Revises: 381f9171486b
Create Date: 2024-08-26 15:30:41.560259

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '472bfcc03388'
down_revision: Union[str, None] = '381f9171486b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
