"""initial migration

Revision ID: 393e65e87110
Revises: 5a86bfa92b30
Create Date: 2020-02-08 19:03:48.991735

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '393e65e87110'
down_revision = '5a86bfa92b30'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('file', sa.Column('auteur', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('file', 'auteur')
    # ### end Alembic commands ###
