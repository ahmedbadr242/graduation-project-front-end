"""empty message

Revision ID: a180071a497c
Revises: bc72967cffb5
Create Date: 2021-02-23 11:37:30.819560

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a180071a497c'
down_revision = 'bc72967cffb5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('class',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cls_name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_class_cls_name'), 'class', ['cls_name'], unique=False)
    op.drop_index('ix_student_std_class', table_name='student')
    op.create_foreign_key(None, 'student', 'class', ['std_class'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'student', type_='foreignkey')
    op.create_index('ix_student_std_class', 'student', ['std_class'], unique=False)
    op.drop_index(op.f('ix_class_cls_name'), table_name='class')
    op.drop_table('class')
    # ### end Alembic commands ###
