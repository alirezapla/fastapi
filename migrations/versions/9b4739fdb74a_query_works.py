"""query works

Revision ID: 9b4739fdb74a
Revises: 65f838bc1e58
Create Date: 2021-12-12 15:16:10.204304

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel             


# revision identifiers, used by Alembic.
revision = '9b4739fdb74a'
down_revision = '65f838bc1e58'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('query', sa.Column('dated', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_query_dated'), 'query', ['dated'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_query_dated'), table_name='query')
    op.drop_column('query', 'dated')
    # ### end Alembic commands ###