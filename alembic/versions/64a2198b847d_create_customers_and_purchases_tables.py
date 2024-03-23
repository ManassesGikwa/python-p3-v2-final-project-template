"""create customers and purchases tables

Revision ID: 64a2198b847d
Revises: d1fada3135fb
Create Date: 2024-03-22 14:52:20.440723

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64a2198b847d'
down_revision = 'd1fada3135fb'
branch_labels = None
depends_on = None


def upgrade():
    connection = op.get_bind()
    inspector = sa.inspect(connection)
    
    if 'customers' not in inspector.get_table_names():
        op.create_table(
            "customers",
            sa.Column("customerid", sa.Integer, primary_key=True),
            sa.Column("FirstName", sa.String),
            sa.Column("LastName", sa.String),
        )
        
    if 'purchases' not in inspector.get_table_names():
        op.create_table(
            "purchases",
            sa.Column("purchaseid", sa.Integer, primary_key=True),
            sa.Column("customerid", sa.Integer, sa.ForeignKey("customers.customerid")),
            sa.Column("product", sa.String),
            sa.Column("price", sa.Float),
        )


def downgrade():
    op.drop_table("purchases")
    op.drop_table("customers")
