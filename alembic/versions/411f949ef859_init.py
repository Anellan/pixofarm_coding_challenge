"""Init

Revision ID: 411f949ef859
Revises: 
Create Date: 2021-10-30 18:41:47.256180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '411f949ef859'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('continent',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_continent_id'), 'continent', ['id'], unique=False)
    op.create_table('location',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('location_name', sa.String(), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('altitude', sa.Float(), nullable=True),
    sa.Column('continent_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['continent_id'], ['continent.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_location_id'), 'location', ['id'], unique=False)
    op.create_table('timeseries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.Integer(), nullable=True),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['location.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_timeseries_id'), 'timeseries', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_timeseries_id'), table_name='timeseries')
    op.drop_table('timeseries')
    op.drop_index(op.f('ix_location_id'), table_name='location')
    op.drop_table('location')
    op.drop_index(op.f('ix_continent_id'), table_name='continent')
    op.drop_table('continent')
    # ### end Alembic commands ###
