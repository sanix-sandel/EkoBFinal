"""initial migration

Revision ID: 3a1ffe22c536
Revises: c4b4d3a4f082
Create Date: 2019-11-06 03:56:50.448759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a1ffe22c536'
down_revision = 'c4b4d3a4f082'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('file', sa.Column('img_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('file', 'img_id')
    # ### end Alembic commands ###
