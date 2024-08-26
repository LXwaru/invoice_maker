"""empty message

Revision ID: 22c58fb10d65
Revises: a4781557626e
Create Date: 2024-08-25 13:04:01.235666

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '22c58fb10d65'
down_revision: Union[str, None] = 'a4781557626e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
