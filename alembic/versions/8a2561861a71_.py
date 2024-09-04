"""empty message

Revision ID: 8a2561861a71
Revises: ef6dda44a174
Create Date: 2024-09-03 15:08:20.597206

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8a2561861a71'
down_revision: Union[str, None] = 'ef6dda44a174'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
