"""First migration

Revision ID: 25ae6f2901f3
Revises: 
Create Date: 2022-01-06 16:50:30.833900

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25ae6f2901f3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('booked_cars',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=20), nullable=False),
    sa.Column('lastname', sa.String(length=20), nullable=False),
    sa.Column('address', sa.String(length=40), nullable=False),
    sa.Column('mobile_number', sa.String(length=20), nullable=False),
    sa.Column('car', sa.String(length=20), nullable=False),
    sa.Column('from_date', sa.String(length=20), nullable=False),
    sa.Column('to_date', sa.String(length=20), nullable=False),
    sa.Column('booked_status', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_booked_cars'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('booked_cars')
    # ### end Alembic commands ###
