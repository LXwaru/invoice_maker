"""empty message

Revision ID: d15f5a8a2f9a
Revises: db352439d06d
Create Date: 2024-08-16 15:36:26.860874

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd15f5a8a2f9a'
down_revision: Union[str, None] = 'db352439d06d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
