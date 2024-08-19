"""empty message

Revision ID: a5ffa6f99e06
Revises: e5afb5d60304
Create Date: 2024-08-18 22:45:34.984829

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a5ffa6f99e06'
down_revision: Union[str, None] = 'e5afb5d60304'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
