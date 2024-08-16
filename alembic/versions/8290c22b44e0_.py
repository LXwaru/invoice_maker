"""empty message

Revision ID: 8290c22b44e0
Revises: e74adb26a262
Create Date: 2024-08-16 14:18:06.044233

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8290c22b44e0'
down_revision: Union[str, None] = 'e74adb26a262'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
