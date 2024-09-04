"""empty message

Revision ID: bab767b5d280
Revises: d526caeaaa38
Create Date: 2024-09-04 16:19:44.628753

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bab767b5d280'
down_revision: Union[str, None] = 'd526caeaaa38'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
