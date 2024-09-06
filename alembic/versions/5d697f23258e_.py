"""empty message

Revision ID: 5d697f23258e
Revises: c62fb92b3579
Create Date: 2024-09-05 15:39:18.861439

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5d697f23258e'
down_revision: Union[str, None] = 'c62fb92b3579'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
