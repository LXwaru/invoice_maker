"""empty message

Revision ID: 1a0f7ee0ff0f
Revises: 415119276571
Create Date: 2024-08-27 21:55:46.240155

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1a0f7ee0ff0f'
down_revision: Union[str, None] = '415119276571'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
