"""empty message

Revision ID: 48a8ab6a6ece
Revises: 743cedaa8fef
Create Date: 2024-12-03 19:18:38.565554

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "48a8ab6a6ece"
down_revision: Union[str, None] = "743cedaa8fef"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("role", "scopes")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "role",
        sa.Column(
            "scopes",
            postgresql.JSONB(astext_type=sa.Text()),
            autoincrement=False,
            nullable=False,
        ),
    )
    # ### end Alembic commands ###
