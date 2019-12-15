"""initial migrate

Revision ID: 54e2fe5249f2
Revises: 8a490d82490d
Create Date: 2019-11-24 19:13:30.098645

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54e2fe5249f2'
down_revision = '8a490d82490d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('reads', sa.Integer(), nullable=True))
    op.drop_column('post', '_reads')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('_reads', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('post', 'reads')
    # ### end Alembic commands ###
