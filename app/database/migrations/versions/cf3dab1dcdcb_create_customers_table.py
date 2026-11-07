"""Create customers table

Revision ID: cf3dab1dcdcb
Revises: 2f76512db106
Create Date: 2026-11-07 20:51:04.119759

"""
from typing import Sequence, Union

import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cf3dab1dcdcb'
down_revision: Union[str, Sequence[str], None] = '2f76512db106'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

from alembic import op


def upgrade() -> None:
    op.execute("""
        CREATE TABLE customers (
            id UUID PRIMARY KEY,
            name VARCHAR(150) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            phone VARCHAR(20),
            created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
        );
    """)


def downgrade() -> None:
    op.execute("""
        DROP TABLE customers;
    """)