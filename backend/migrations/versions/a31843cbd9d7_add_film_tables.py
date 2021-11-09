"""add film tables

Revision ID: a31843cbd9d7
Revises: 
Create Date: 2021-11-09 09:02:29.085385

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a31843cbd9d7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('actors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('directors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('films',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('runtime', sa.Integer(), nullable=True),
    sa.Column('plot', sa.Text(), nullable=True),
    sa.Column('imdb_id', sa.String(length=255), nullable=True),
    sa.Column('imdb_title', sa.String(length=255), nullable=True),
    sa.Column('imdb_year', sa.Integer(), nullable=True),
    sa.Column('imdb_rating', sa.Float(), nullable=True),
    sa.Column('imdb_low_confidence', sa.Boolean(), nullable=True),
    sa.Column('mtc_title', sa.String(length=255), nullable=True),
    sa.Column('mtc_year', sa.Integer(), nullable=True),
    sa.Column('mtc_rating', sa.Integer(), nullable=True),
    sa.Column('mtc_low_confidence', sa.Boolean(), nullable=True),
    sa.Column('rt_title', sa.String(length=255), nullable=True),
    sa.Column('rt_year', sa.Integer(), nullable=True),
    sa.Column('rt_tomato_rating', sa.Integer(), nullable=True),
    sa.Column('rt_low_confidence', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('genres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('films_actors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('actor', sa.Integer(), nullable=True),
    sa.Column('film', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['actor'], ['actors.id'], name='fk_films_actors_actors_actor_id', onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['film'], ['films.id'], name='fk_films_actors_films_film_id', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('films_directors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('director', sa.Integer(), nullable=True),
    sa.Column('film', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['director'], ['directors.id'], name='fk_films_directors_directors_director_id', onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['film'], ['films.id'], name='fk_films_directors_films_film_id', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('films_genres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('genre', sa.Integer(), nullable=True),
    sa.Column('film', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['film'], ['films.id'], name='fk_films_genres_films_film_id', onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['genre'], ['genres.id'], name='fk_films_genres_genres_genre_id', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('films_genres')
    op.drop_table('films_directors')
    op.drop_table('films_actors')
    op.drop_table('genres')
    op.drop_table('films')
    op.drop_table('directors')
    op.drop_table('actors')
    # ### end Alembic commands ###