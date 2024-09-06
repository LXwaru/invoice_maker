"""empty message

Revision ID: c9e4f00a7766
Revises: 908b862dfd9d
Create Date: 2024-09-05 16:24:42.589137

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c9e4f00a7766'
down_revision: Union[str, None] = '908b862dfd9d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
