"""create customers table

Revision ID: 24a949e86f53
Revises: 
Create Date: 2024-03-22 14:46:16.987251

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24a949e86f53'
down_revision = None
branch_labels = None
depends_on = None


# Upgrade function
def upgrade():
    connection = op.get_bind()
    inspector = sa.inspect(connection)
    # Check if the table exists before creating it
    if 'customers' not in inspector.get_table_names():
        op.create_table(
            "customers",
            sa.Column("customerid", sa.Integer, primary_key=True),
            sa.Column("FirstName", sa.String),
            sa.Column("LastName", sa.String),
        )


def downgrade() -> None:
    op.drop_table("customers")
