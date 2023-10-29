import pytest
from BBapp import app

@pytest.fixture
def client(): #Peter
    client = app.test_client()
    yield client

def signup(client, email, name, phone, password, confirmPassword, clubRepresentative, clubName, clubRole): #Peter
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

def test_signup(client): #Peter
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

def login(client, email, password): #Nuova
    return client.post('/login', data=dict(
        email=email,
        password=password
    ), follow_redirects=True)

def test_login(client): #Nuova
    # Test if login page renders correctly
    response = client.get('/login')
    assert response.status_code == 200, "Login page did not render correctly"

    # Test for invalid email login
    response = login(client, 'invalid@notutoronto.com', 'password')
    assert response.status_code == 200, "Invalid email login did not redirect to login page"

    # Test for incorrect password login
    response = login(client, 'valid@utoronto.ca', 'wrongpassword')
    assert response.status_code == 200, "Incorrect password login did not redirect to login page"

    # Test for successful login
    response = login(client, 'valid@utoronto.ca', 'password')
    assert b'user' in response.data, "Successful login did not redirect to user page or did not show expected content"

