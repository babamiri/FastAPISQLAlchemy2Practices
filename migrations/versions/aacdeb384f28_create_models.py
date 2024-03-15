"""create models

Revision ID: aacdeb384f28
Revises: 
Create Date: 2024-03-15 14:46:10.334692

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aacdeb384f28'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('course',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student_corse',
    sa.Column('student_id', sa.UUID(), nullable=True),
    sa.Column('course_id', sa.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['course.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], )
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student_corse')
    op.drop_table('student')
    op.drop_table('course')
    # ### end Alembic commands ###
