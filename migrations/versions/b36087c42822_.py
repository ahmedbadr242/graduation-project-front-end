"""empty message

Revision ID: b36087c42822
Revises: e93dc6d5b908
Create Date: 2021-03-17 13:25:09.753823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b36087c42822'
down_revision = 'e93dc6d5b908'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student_attendance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('std_name', sa.String(length=64), nullable=True),
    sa.Column('std_class', sa.String(length=64), nullable=True),
    sa.Column('teacher', sa.String(length=64), nullable=True),
    sa.Column('attendance', sa.String(length=64), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student_attendance')
    # ### end Alembic commands ###