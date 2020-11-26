def test_get_all(client, app):
    with app.app_context():
        resp = client.get("/get_all_entrys/products")
        assert b'id' in resp.data
        assert b'name' in resp.data
        assert b'price' in resp.data
        assert b'description' in resp.data
        assert b'image' in resp.data
        assert b'stock' in resp.data