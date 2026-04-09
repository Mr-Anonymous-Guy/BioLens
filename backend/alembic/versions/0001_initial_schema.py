"""initial schema

Revision ID: 0001_initial_schema
Revises:
Create Date: 2026-04-09
"""

from alembic import op

import app.models  # noqa: F401
from app.database import Base

# revision identifiers, used by Alembic.
revision = "0001_initial_schema"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    bind = op.get_bind()
    Base.metadata.create_all(bind=bind)


def downgrade():
    bind = op.get_bind()
    Base.metadata.drop_all(bind=bind)
