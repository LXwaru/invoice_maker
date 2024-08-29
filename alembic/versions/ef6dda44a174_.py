"""empty message

Revision ID: ef6dda44a174
Revises: 1a0f7ee0ff0f
Create Date: 2024-08-28 22:36:55.695381

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ef6dda44a174'
down_revision: Union[str, None] = '1a0f7ee0ff0f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
