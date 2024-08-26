"""empty message

Revision ID: d9f012499727
Revises: dd955689abe8
Create Date: 2024-08-26 14:21:03.983339

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd9f012499727'
down_revision: Union[str, None] = 'dd955689abe8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
