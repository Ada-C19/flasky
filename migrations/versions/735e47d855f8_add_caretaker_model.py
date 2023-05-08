"""Add caretaker model

Revision ID: 735e47d855f8
Revises: e83e98f0abec
Create Date: 2023-05-08 13:24:08.076272

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '735e47d855f8'
down_revision = 'e83e98f0abec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('caretaker',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('caretaker')
    # ### end Alembic commands ###
