"""initiate migrate

Revision ID: 003d9e62dce9
Revises: 6e8b5cfaf3f3
Create Date: 2019-12-25 11:28:56.169896

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '003d9e62dce9'
down_revision = '6e8b5cfaf3f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('nbrnotifs', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'nbrnotifs')
    # ### end Alembic commands ###