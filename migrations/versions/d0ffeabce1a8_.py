"""empty message

Revision ID: d0ffeabce1a8
Revises: 2578fbfa7840
Create Date: 2020-12-11 00:59:00.389324

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0ffeabce1a8'
down_revision = '2578fbfa7840'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('script', 'file_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('script', sa.Column('file_name', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
