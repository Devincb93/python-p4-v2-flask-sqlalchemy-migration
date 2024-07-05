"""add Department

Revision ID: 535d8def643d
Revises: 14943ae713ae
Create Date: 2024-07-04 21:33:52.351089

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '535d8def643d'
down_revision = '14943ae713ae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('department')
    # ### end Alembic commands ###
