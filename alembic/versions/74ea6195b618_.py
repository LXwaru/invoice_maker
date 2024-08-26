"""empty message

Revision ID: 74ea6195b618
Revises: d9f012499727
Create Date: 2024-08-26 14:31:36.424698

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '74ea6195b618'
down_revision: Union[str, None] = 'd9f012499727'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
