"""empty message

Revision ID: 03416bea4ac1
Revises: 53db0070ba46
Create Date: 2022-06-13 17:32:30.641598

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03416bea4ac1'
down_revision = '53db0070ba46'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'Artist', ['name'])
    op.create_unique_constraint(None, 'Venue', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Venue', type_='unique')
    op.drop_constraint(None, 'Artist', type_='unique')
    # ### end Alembic commands ###
