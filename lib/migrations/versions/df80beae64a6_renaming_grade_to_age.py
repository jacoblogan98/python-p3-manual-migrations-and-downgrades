"""Renaming grade to age

Revision ID: df80beae64a6
Revises: 791279dd0760
Create Date: 2023-02-01 15:48:19.818870

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df80beae64a6'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'grade', new_column_name='age')


def downgrade() -> None:
    op.alter_column('students', 'age', new_column_name='grade')
