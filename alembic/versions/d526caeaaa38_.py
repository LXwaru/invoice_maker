"""empty message

Revision ID: d526caeaaa38
Revises: ca6ef72b9e23
Create Date: 2024-09-04 15:57:54.926599

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd526caeaaa38'
down_revision: Union[str, None] = 'ca6ef72b9e23'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
