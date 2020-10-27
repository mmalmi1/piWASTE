import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    """
    Get a database instance, and opens a connection to database if needed.

    return: database instance
    """
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    """
    Close the database connection
    """
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    """
    Initializes the database from schema.sql
    """
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

    push_into_db(f'INSERT INTO users (username, password, access_level) VALUES ("admin", "admin", "1")')

def get_from_db(command):
    """
    Execute given SQL query, and return the result.

    return: iterable of selected rows in a dict format with column-value pairs.
    """
    print(f"Execute {command}")
    db = get_db()
    return db.execute(command)

def push_into_db(command):
    """ 
    Execute the SQL query and commits the changes to database.
    Does not return anything. To get things from database, use "get_from_db"
    """
    try: 
        print(f"Execute {command}")
        db = get_db()
        db.execute(command)
        db.commit()
    except sqlite3.IntegrityError:
        print("push_into_db failed, entry not unique")
        return False
    return True

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


@click.command('init-db') # adds "flask init-db" command
@with_appcontext
def init_db_command():
    """
    Creates a new, clean database file.
    Clear the existing data and create new tables.
    """
    init_db()
    click.echo('Initialized the database.')