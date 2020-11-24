def test_login_logout(client):
    resp = client.post(
            '/login',
            data={'username': 'testuser', 'password': 'testuser'},
            follow_redirects=True
        )
    # Check that it redirects after a successful login
    assert resp.status_code == 200
    assert b'Welcome' in resp.data
    # Log out button should be available after logging in
    assert b'/logout' in resp.data

    resp = client.get('/logout', follow_redirects=True)
    # Logout shoukd redirect to index
    assert resp.status_code == 200
    assert b'Welcome' in resp.data

def test_login_page(client):
    login_page = client.get("/login")
    assert login_page.status_code == 200
    assert b'username' in login_page.data
    assert b'password' in login_page.data