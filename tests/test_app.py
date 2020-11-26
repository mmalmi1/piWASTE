from app import create_app

def test_index(client, app):
    # Make sure testing is not the default state, and the config mapping works
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing
