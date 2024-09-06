"""empty message

Revision ID: bc2316763448
Revises: 6bf6dc9a7b17
Create Date: 2024-09-05 15:35:42.974129

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bc2316763448'
down_revision: Union[str, None] = '6bf6dc9a7b17'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
