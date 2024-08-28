"""empty message

Revision ID: 381f9171486b
Revises: 31a56a3a1a5a
Create Date: 2024-08-26 15:30:22.183233

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '381f9171486b'
down_revision: Union[str, None] = '31a56a3a1a5a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
