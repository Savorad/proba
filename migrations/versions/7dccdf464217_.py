"""empty message

Revision ID: 7dccdf464217
Revises: a5316d4a7b73
Create Date: 2019-07-09 16:11:27.021811

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7dccdf464217'
down_revision = 'a5316d4a7b73'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    measurement = table('measurement',
        column('id', sa.Integer),
        column('air_quality', sa.Float),
        column('humidity', sa.Float),
        column('temperature', sa.Float),
        column('timestamp', sa.DateTime)
    )
    op.add_column('measurement', sa.Column('timestamp', sa.DateTime(timezone=True), server_default='now()', nullable=False))
    op.alter_column('measurement', 'air_quality',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=False)
    op.alter_column('measurement', 'humidity',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=False)
    op.alter_column('measurement', 'temperature',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=False)

    op.bulk_insert(measurement, [{'air_quality':1.0, 'temperature':1.0,'humidity':1.0}, 
            {'air_quality':2.0, 'temperature':2.0,'humidity':2.0},
            {'air_quality':3.0, 'temperature':3.0,'humidity':3.0},
            {'air_quality':4.0, 'temperature':4.0,'humidity':4.0},
            {'air_quality':5.0, 'temperature':5.0,'humidity':5.0}])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('measurement', 'temperature',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=True)
    op.alter_column('measurement', 'humidity',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=True)
    op.alter_column('measurement', 'air_quality',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=True)
    op.drop_column('measurement', 'timestamp')
    # ### end Alembic commands ###
