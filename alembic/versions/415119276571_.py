"""empty message

Revision ID: 415119276571
Revises: 7bf76bdd3529
Create Date: 2024-08-27 16:06:49.920799

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '415119276571'
down_revision: Union[str, None] = '7bf76bdd3529'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
