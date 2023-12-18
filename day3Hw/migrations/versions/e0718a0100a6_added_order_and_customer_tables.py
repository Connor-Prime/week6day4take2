"""added order and customer tables

Revision ID: e0718a0100a6
Revises: de06db95b168
Create Date: 2023-12-17 17:43:33.104030

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0718a0100a6'
down_revision = 'de06db95b168'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customer',
    sa.Column('cust_id', sa.String(), nullable=False),
    sa.Column('date_created', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('cust_id')
    )
    op.create_table('order',
    sa.Column('order_id', sa.String(), nullable=False),
    sa.Column('order_total', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('order_id')
    )
    op.create_table('prod_order',
    sa.Column('prodorder_id', sa.String(), nullable=False),
    sa.Column('prod_id', sa.String(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('order_id', sa.String(), nullable=False),
    sa.Column('cust_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['cust_id'], ['customer.cust_id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['order.order_id'], ),
    sa.ForeignKeyConstraint(['prod_id'], ['product.prod_id'], ),
    sa.PrimaryKeyConstraint('prodorder_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('prod_order')
    op.drop_table('order')
    op.drop_table('customer')
    # ### end Alembic commands ###
