"""initial migration

Revision ID: ebd87b02f0a4
Revises: 6c041f0e2b04
Create Date: 2019-09-27 04:10:12.603681

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ebd87b02f0a4'
down_revision = '6c041f0e2b04'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('file', sa.Column('downloads', sa.Integer(), nullable=True))
    op.drop_column('file', '_downloads')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('file', sa.Column('_downloads', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('file', 'downloads')
    # ### end Alembic commands ###