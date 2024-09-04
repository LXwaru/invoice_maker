"""empty message

Revision ID: 5fc5cc5ab268
Revises: 77e5ec3a228b
Create Date: 2024-09-04 14:23:13.240460

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5fc5cc5ab268'
down_revision: Union[str, None] = '77e5ec3a228b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
