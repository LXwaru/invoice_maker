"""empty message

Revision ID: bdf81195f556
Revises: 21d27fbe9984
Create Date: 2024-09-05 15:52:23.291247

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bdf81195f556'
down_revision: Union[str, None] = '21d27fbe9984'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
