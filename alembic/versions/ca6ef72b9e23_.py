"""empty message

Revision ID: ca6ef72b9e23
Revises: 152b58c4c34d
Create Date: 2024-09-04 15:19:43.856126

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ca6ef72b9e23'
down_revision: Union[str, None] = '152b58c4c34d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
