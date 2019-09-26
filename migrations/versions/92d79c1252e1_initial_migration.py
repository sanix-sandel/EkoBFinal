"""initial migration

Revision ID: 92d79c1252e1
Revises: 684545a5d728
Create Date: 2019-09-18 10:36:26.138050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92d79c1252e1'
down_revision = '684545a5d728'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('reads', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'reads')
    # ### end Alembic commands ###