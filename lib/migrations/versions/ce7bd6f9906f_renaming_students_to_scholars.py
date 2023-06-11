"""Renaming students to scholars

Revision ID: ce7bd6f9906f
Revises: 791279dd0760
Create Date: 2023-06-11 10:29:19.458911

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce7bd6f9906f'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')

