"""Create phone number for user column

Revision ID: 32d8ddb581b4
Revises: 
Create Date: 2026-01-03 22:40:50.849648

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '32d8ddb581b4'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable = True))


def downgrade() -> None:
    """Downgrade schema."""
    pass
