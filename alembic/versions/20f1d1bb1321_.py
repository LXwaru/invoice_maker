"""empty message

Revision ID: 20f1d1bb1321
Revises: d15f5a8a2f9a
Create Date: 2024-08-16 15:40:42.508076

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '20f1d1bb1321'
down_revision: Union[str, None] = 'd15f5a8a2f9a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
