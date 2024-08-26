"""empty message

Revision ID: dd955689abe8
Revises: ec0fb0151f63
Create Date: 2024-08-26 13:56:49.823555

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dd955689abe8'
down_revision: Union[str, None] = 'ec0fb0151f63'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
