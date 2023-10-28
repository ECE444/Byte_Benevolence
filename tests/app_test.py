import pytest
from BBapp import app

@pytest.fixture
def client():
    client = app.test_client()
    yield client

def signup(client, email, name, phone, password, confirmPassword, clubRepresentative, clubName, clubRole):
    return client.post('/signup', data=dict(
        email=email,
        name=name,
        phone=phone,
        password=password,
        confirmPassword=confirmPassword,
        clubRepresentative=clubRepresentative,
        clubName=clubName,
        clubRole=clubRole
    ), follow_redirects=False)

def test_signup(client): 
    """Test signup route"""
    rv = signup(client, 'test@mail.utoronto.ca', 'test', '1234567890', 'password', 'noMatchingPassword', 'No', '', '') #no matching passwords
    assert rv.status_code == 200 and "Passwords do not match" in str(rv.data)
    rv = signup(client, 'test@gmail.com', 'test', '1234567890', 'password', 'password', 'No', '', '') #non uoft email
    assert rv.status_code == 200 and "Please use a valid UofT email address" in str(rv.data)
    rv = signup(client, 'test@mail.utoronto.ca', 'test', '1234567890', 'password', 'password', 'Yes', '', '') #empty club name
    assert rv.status_code == 200 and "Please enter a club name" in str(rv.data)
    rv = signup(client, 'test@mail.utoronto.ca', 'test', '1234567890', 'password', 'password', 'No', '', '') #valid signup of non club representative
    assert rv.status_code == 302 and rv.location == '/user'
    rv = signup(client, 'test@mail.utoronto.ca', 'test', '1234567890', 'password', 'password', 'Yes', 'Developer Club', 'President') #valid signup of club representative
    assert rv.status_code == 302 and rv.location == '/user'

