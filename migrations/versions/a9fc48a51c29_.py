"""empty message

Revision ID: a9fc48a51c29
Revises: 
Create Date: 2020-12-19 15:17:31.334857

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9fc48a51c29'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('module',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('file_name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('preference',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('resources',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('file_name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('script',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('file_name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('preference_module',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('preference_id', sa.Integer(), nullable=False),
    sa.Column('module_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['module_id'], ['module.id'], ),
    sa.ForeignKeyConstraint(['preference_id'], ['preference.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('preference_resource',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('preference_id', sa.Integer(), nullable=False),
    sa.Column('resource_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['preference_id'], ['preference.id'], ),
    sa.ForeignKeyConstraint(['resource_id'], ['resources.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('preference_script',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('preference_id', sa.Integer(), nullable=True),
    sa.Column('script_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['preference_id'], ['preference.id'], ),
    sa.ForeignKeyConstraint(['script_id'], ['script.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('preference_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('preference_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['preference_id'], ['preference.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('curent_user_preference',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('preference_id', sa.Integer(), nullable=True),
    sa.Column('preference_user_id', sa.Integer(), nullable=True),
    sa.Column('current_user_preference', sa.Boolean(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['preference_id'], ['preference.id'], ),
    sa.ForeignKeyConstraint(['preference_user_id'], ['preference_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('curent_user_preference')
    op.drop_table('preference_user')
    op.drop_table('preference_script')
    op.drop_table('preference_resource')
    op.drop_table('preference_module')
    op.drop_table('user')
    op.drop_table('script')
    op.drop_table('resources')
    op.drop_table('preference')
    op.drop_table('module')
    # ### end Alembic commands ###
