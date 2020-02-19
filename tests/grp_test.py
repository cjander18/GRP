from conftest import client

def hello_whale(client):
    return client.get('/')

def test_hello_whale(client):
    """Make sure login and logout works."""

    rv = hello_whale(client)
    print(rv.data)
    assert b'Whale, hello there!!' in rv.data
