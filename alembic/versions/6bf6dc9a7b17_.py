"""empty message

Revision ID: 6bf6dc9a7b17
Revises: 5cd8da948ee6
Create Date: 2024-09-05 15:20:16.009747

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6bf6dc9a7b17'
down_revision: Union[str, None] = '5cd8da948ee6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
