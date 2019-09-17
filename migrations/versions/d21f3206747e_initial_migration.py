"""initial migration

Revision ID: d21f3206747e
Revises: 0acd8f1d00b8
Create Date: 2019-09-17 16:19:49.530896

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd21f3206747e'
down_revision = '0acd8f1d00b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('interests', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'interests')
    # ### end Alembic commands ###