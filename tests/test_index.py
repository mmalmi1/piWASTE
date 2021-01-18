def test_index(client):
    index = client.get("/")
    # Check the statuscode
    assert index.status_code == 200
    # Check that the right asset is returned
    assert b'Welcome to piWASTE!' in index.data

def test_index_links_logged_in(client):
    client.set_cookie('localhost', 'logged_in', 'True')
    # Login redirects to index
    index = client.get("/")
    assert b"/login" in index.data
    assert b"/products" in index.data
    assert b"/profile" in index.data
    assert b"/shopping_cart" in index.data

def test_index_links(client):
    client.set_cookie('localhost', 'logged_in', 'False')
    index = client.get("/")
    assert b"/login" in index.data
    assert b"/products" in index.data
    # TODO: Uncomment these when/if the buttons in front page are disabled when
    # not logged in
    # assert b"/profile" not in index.data
    # assert b"/shopping_cart" not in index.data
