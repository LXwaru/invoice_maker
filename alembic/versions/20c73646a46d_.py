"""empty message

Revision ID: 20c73646a46d
Revises: bdf81195f556
Create Date: 2024-09-05 16:05:03.207890

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '20c73646a46d'
down_revision: Union[str, None] = 'bdf81195f556'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
