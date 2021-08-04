from django.apps import AppConfig
import sqlite3
import json
from pathlib import Path


class MoviesConfig(AppConfig):
    name = 'movies'


# genres = json.loads(Path('movies.json').read_text())

# with sqlite3.connect('db.sqlite3') as conn:
#     command = 'INSERT INTO movies_movie VALUES(?,?,?,?,?,?,?)'
#     for genre in genres:
#         conn.execute(command, tuple(genre.values()))
#     conn.commit()
