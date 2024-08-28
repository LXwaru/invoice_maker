"""empty message

Revision ID: 7bf76bdd3529
Revises: dfff7ae6fad0
Create Date: 2024-08-26 16:28:56.715286

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7bf76bdd3529'
down_revision: Union[str, None] = 'dfff7ae6fad0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
