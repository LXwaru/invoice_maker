"""empty message

Revision ID: 04f7f93a9318
Revises: c9cd6a65cc75
Create Date: 2024-09-05 21:20:50.227600

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '04f7f93a9318'
down_revision: Union[str, None] = 'c9cd6a65cc75'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
