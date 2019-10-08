"""initial migration

Revision ID: a7c204234b4b
Revises: 007a11f20cfc
Create Date: 2019-10-03 22:53:04.559276

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7c204234b4b'
down_revision = '007a11f20cfc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('file', 'cover')
    op.add_column('post', sa.Column('genre', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'genre')
    op.add_column('file', sa.Column('cover', sa.VARCHAR(length=20), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
