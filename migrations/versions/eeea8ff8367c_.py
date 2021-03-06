"""empty message

Revision ID: eeea8ff8367c
Revises: 
Create Date: 2020-03-07 11:37:04.748527

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eeea8ff8367c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('LinRegResults',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('YearsExperience', sa.Float(), nullable=True),
    sa.Column('Prediction', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('monDS')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('monDS',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=True)
    )
    op.drop_table('LinRegResults')
    # ### end Alembic commands ###
