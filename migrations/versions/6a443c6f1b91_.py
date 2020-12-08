"""empty message

Revision ID: 6a443c6f1b91
Revises: 9f0615be7706
Create Date: 2020-12-03 01:16:03.593687

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a443c6f1b91'
down_revision = '9f0615be7706'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
    # ### end Alembic commands ###