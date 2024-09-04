"""empty message

Revision ID: 152b58c4c34d
Revises: 0764ce9b728d
Create Date: 2024-09-04 15:18:55.586208

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '152b58c4c34d'
down_revision: Union[str, None] = '0764ce9b728d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
