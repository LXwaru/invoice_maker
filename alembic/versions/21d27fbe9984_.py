"""empty message

Revision ID: 21d27fbe9984
Revises: 65023517c5fb
Create Date: 2024-09-05 15:51:07.509396

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '21d27fbe9984'
down_revision: Union[str, None] = '65023517c5fb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
