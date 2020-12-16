def test_profile_logged_in(client):
    client.set_cookie('localhost', 'user_id', '99999')
    client.set_cookie('localhost', 'logged_in', 'True')
    page = client.get("/profile")
    assert b'User name' in page.data
    assert b'Email' in page.data
    assert b'Address' in page.data
    assert b'Phone' in page.data

def test_profile_logged_out(client):
    client.set_cookie('localhost', 'user_id', '0')
    client.set_cookie('localhost', 'logged_in', 'False')
    page = client.get("/profile")
    assert page.status_code == 302
    assert b'You should be redirected automatically to target URL' in page.data
    
def test_profile_edit_logged_in(client):
    client.set_cookie('localhost', 'user_id', '99999')
    client.set_cookie('localhost', 'logged_in', 'True')
    page = client.get("/profile/edit")
    assert page.status_code == 200
    assert b'Submit changes' in page.data

def test_profile_edit_logged_out(client):
    client.set_cookie('localhost', 'user_id', '0')
    client.set_cookie('localhost', 'logged_in', 'False')
    page = client.get("/profile/edit")
    assert page.status_code == 401
    assert b'Need to log in to access profile information' in page.data