"""create customers table

Revision ID: 5bdae17aeb27
Revises: 64a2198b847d
Create Date: 2024-03-23 01:20:41.413897

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '5bdae17aeb27'
down_revision = '64a2198b847d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Check if the 'customers' table exists
    if not op.get_context().bind.dialect.has_table(op.get_context().bind, "customers"):
        # Create the 'customers' table
        op.create_table(
            'customers',
            sa.Column('customerid', sa.Integer(), nullable=False),
            sa.Column('FirstName', sa.String(), nullable=True),
            sa.Column('LastName', sa.String(), nullable=True),
            sa.PrimaryKeyConstraint('customerid')
        )


def downgrade() -> None:
    # Drop the 'customers' table
    op.drop_table('customers')
