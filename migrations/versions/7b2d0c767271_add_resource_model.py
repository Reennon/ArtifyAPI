"""add resource model 

Revision ID: 7b2d0c767271
Revises: 417d22f291c9
Create Date: 2020-12-18 18:49:35.200336

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b2d0c767271'
down_revision = '417d22f291c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('preference_resource_resource_id_fkey', 'preference_resource', type_='foreignkey')
    op.drop_column('preference_resource', 'resource_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('preference_resource', sa.Column('resource_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('preference_resource_resource_id_fkey', 'preference_resource', 'module', ['resource_id'], ['id'])
    # ### end Alembic commands ###
