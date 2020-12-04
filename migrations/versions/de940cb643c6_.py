"""empty message

Revision ID: de940cb643c6
Revises: 64f40870f9bd
Create Date: 2020-12-01 15:35:17.884119

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de940cb643c6'
down_revision = '64f40870f9bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('preference',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('script',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('file_name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('preference_module',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('preference_script_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['preference_script_id'], ['module.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('preference_script',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('preference_script_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['preference_script_id'], ['script.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('preference_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('preference_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['preference_id'], ['preference.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('preference_user')
    op.drop_table('preference_script')
    op.drop_table('preference_module')
    op.drop_table('script')
    op.drop_table('preference')
    # ### end Alembic commands ###