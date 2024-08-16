"""empty message

Revision ID: e74adb26a262
Revises: 93105ecf0b16
Create Date: 2024-08-16 14:16:12.729097

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e74adb26a262'
down_revision: Union[str, None] = '93105ecf0b16'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
