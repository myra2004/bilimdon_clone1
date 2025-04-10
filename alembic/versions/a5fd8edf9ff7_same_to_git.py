"""same to git

Revision ID: a5fd8edf9ff7
Revises: fae78eb4ee21
Create Date: 2025-04-10 20:24:44.826283

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a5fd8edf9ff7'
down_revision: Union[str, None] = 'fae78eb4ee21'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('games', sa.Column('user_id', sa.Integer(), nullable=False))
    op.drop_constraint('games_owner_id_fkey', 'games', type_='foreignkey')
    op.create_foreign_key(None, 'games', 'users', ['user_id'], ['id'])
    op.drop_column('games', 'owner_id')
    op.add_column('questions', sa.Column('user_id', sa.Integer(), nullable=False))
    op.drop_constraint('questions_owner_id_fkey', 'questions', type_='foreignkey')
    op.drop_constraint('questions_game_id_fkey', 'questions', type_='foreignkey')
    op.create_foreign_key(None, 'questions', 'users', ['user_id'], ['id'])
    op.drop_column('questions', 'game_id')
    op.drop_column('questions', 'owner_id')
    op.alter_column('users', 'first_name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('users', 'last_name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'last_name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('users', 'first_name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.add_column('questions', sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('questions', sa.Column('game_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'questions', type_='foreignkey')
    op.create_foreign_key('questions_game_id_fkey', 'questions', 'games', ['game_id'], ['id'])
    op.create_foreign_key('questions_owner_id_fkey', 'questions', 'users', ['owner_id'], ['id'])
    op.drop_column('questions', 'user_id')
    op.add_column('games', sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'games', type_='foreignkey')
    op.create_foreign_key('games_owner_id_fkey', 'games', 'users', ['owner_id'], ['id'])
    op.drop_column('games', 'user_id')
    # ### end Alembic commands ###
