"""empty message

Revision ID: 1e905c65337a
Revises: 38a6026cda33
Create Date: 2017-06-11 09:44:02.153201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e905c65337a'
down_revision = '38a6026cda33'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blacklist_tokens',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=500), nullable=False),
    sa.Column('blacklisted_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.add_column(u'users', sa.Column('admin', sa.Boolean(), nullable=False))
    op.add_column(u'users', sa.Column('registered_on', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'users', 'registered_on')
    op.drop_column(u'users', 'admin')
    op.drop_table('blacklist_tokens')
    # ### end Alembic commands ###
