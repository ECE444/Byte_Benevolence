import pytest
from user_class import user

testUser = user("test", "user", "test.user@mail.utoronto.ca", "1234567890", 1, 1, "President")

def test_user_dictionary(): #Lucas 
    dict = testUser.dictionary()
    assert dict == {'firstname': "test", 'lastname': "user", 'email': "test.user@mail.utoronto.ca", 'phone': "1234567890", 'userID': 1, 'orgID': 1, 'orgRole': "President"}

def test_user_mutators(): #Lucas
    firstname = testUser.get_firstname()
    assert firstname == "test"
    lastname = testUser.get_lastname()
    assert lastname == "user"
    email = testUser.get_email()
    assert email == "test.user@mail.utoronto.ca"
    phone = testUser.get_phone()
    assert phone == "1234567890"
    testUser.set_userID(2)
    userID = testUser.get_userID()
    assert userID == 2
    testUser.set_orgID(2)
    orgID = testUser.get_orgID()
    assert orgID == 2
    testUser.set_orgRole("Vice President")
    orgRole = testUser.get_orgRole()
    assert orgRole == "Vice President"
