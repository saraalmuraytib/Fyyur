"""empty message

Revision ID: 9634b83c22f5
Revises: 86c4a4f0b2e9
Create Date: 2021-06-20 06:50:59.853748

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9634b83c22f5'
down_revision = '86c4a4f0b2e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('seeking_venue', sa.Boolean(), nullable=True))
    op.drop_column('Artist', 'looking_for_venues')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('looking_for_venues', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('Artist', 'seeking_venue')
    # ### end Alembic commands ###