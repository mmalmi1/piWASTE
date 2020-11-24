def test_empty_cart(client, app):
    with app.app_context():
        client.set_cookie('localhost', 'user_id', '99999')
        client.set_cookie('localhost', 'logged_in', 'True')
        client.set_cookie('localhost', 'access_level', '1')
        client.set_cookie('localhost', 'shopping_cart', r"")
        resp = client.get("/shopping_cart")
        assert b'Total amount of' in resp.data

def test_cart(client, app):
    with app.app_context():
        client.set_cookie('localhost', 'user_id', '99999')
        client.set_cookie('localhost', 'logged_in', 'True')
        client.set_cookie('localhost', 'access_level', '1')
        client.set_cookie('localhost', 'shopping_cart', r"{99999: 10}")
        resp = client.get("/shopping_cart")
        assert resp.status_code == 200
        assert b'In total:' in resp.data

def test_get_cart_contents(client, app):
    with app.app_context():
        client.set_cookie('localhost', 'shopping_cart', r"{99999: 13}")
        expected = {
            "99999": {
                "name": "TestProduct",
                "price": 15.1,
                "description": "This is a test description",
                "amount": 13
            }
        }
        assert expected == eval(client.get("/get_shopping_cart").data.decode())