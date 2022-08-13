"""add user table

Revision ID: 251108d4eea7
Revises: 8d2a758cbab3
Create Date: 2022-08-13 17:12:50.758166

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '251108d4eea7'
down_revision = '8d2a758cbab3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              nullable=False, server_default=sa.text('now()')),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
