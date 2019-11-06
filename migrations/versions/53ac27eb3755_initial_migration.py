"""initial migration

Revision ID: 53ac27eb3755
Revises: 0d70d788deca
Create Date: 2019-10-29 02:38:32.634027

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53ac27eb3755'
down_revision = '0d70d788deca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reply',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_posted', sa.DateTime(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('comment_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['comment_id'], ['comment.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reply')
    # ### end Alembic commands ###