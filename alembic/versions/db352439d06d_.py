"""empty message

Revision ID: db352439d06d
Revises: 8290c22b44e0
Create Date: 2024-08-16 15:35:07.456507

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'db352439d06d'
down_revision: Union[str, None] = '8290c22b44e0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
