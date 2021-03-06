"""empty message

Revision ID: 38a6026cda33
Revises: cd44bfc7b992
Create Date: 2017-06-04 14:24:53.012758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38a6026cda33'
down_revision = 'cd44bfc7b992'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bucketlists', sa.Column('created_by', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'bucketlists', 'users', ['created_by'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'bucketlists', type_='foreignkey')
    op.drop_column('bucketlists', 'created_by')
    # ### end Alembic commands ###
