"""updated 6/23/2021

Revision ID: 95492db630fe
Revises: f441f865dc29
Create Date: 2021-06-23 22:09:24.696826

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95492db630fe'
down_revision = 'f441f865dc29'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('car',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('doors', sa.Integer(), nullable=True),
    sa.Column('make', sa.String(length=20), nullable=True),
    sa.Column('model', sa.String(length=20), nullable=True),
    sa.Column('series', sa.String(length=20), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('color', sa.String(length=20), nullable=True),
    sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('car')
    # ### end Alembic commands ###
