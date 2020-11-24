import sqlite3
import pytest

from app.db import get_db, get_from_db, push_into_db, close_db, init_db, \
    make_dicts
    
def test_get_and_close_db(app):
    with app.app_context():
        db = get_db()
        assert db is get_db()

    with pytest.raises(sqlite3.ProgrammingError) as e:
        db.execute('SELECT 1')

    assert 'closed' in str(e.value)


def test_init_db_command(runner, monkeypatch):
    class Test(object):
        boolean = False

    def fake_init_db():
        Test.boolean = True

    monkeypatch.setattr('app.db.init_db', fake_init_db)
    result = runner.invoke(args=['init-db'])
    assert 'Initialized' in result.output
    assert Test.boolean

def test_get_from_db(app):
    with app.app_context():
        case = {
            "name": "Teddy",
            "price": 10.15,
            "description": "Little broken teddy trying to find new home. Might need some" + \
                           " additional cleaning. Otherwise in perfect condition",
            "image": 'assets/broken_teddy1.png',
            "stock": 10
        }
        rows = get_from_db("SELECT * FROM products")
        row = rows.fetchone()
        for key, value in case.items():
            assert row[key] == value

def test_push_into_db(app):
    with app.app_context():
        name = "test"
        price = 10
        description = "description"
        image = "imagestring"
        stock = 10
        command = f'INSERT INTO products (name, price, description, image, stock) VALUES ("{name}", "{price}", "{description}", "{image}", "{stock}")'
        assert push_into_db(command)
        assert bool(get_from_db(f'SELECT * FROM products WHERE name = "{name}" AND price = {price} AND description = "{description}" AND image = "{image}" AND stock = {stock}'))