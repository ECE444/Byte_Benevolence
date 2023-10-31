import unittest
from datetime import datetime
from organization_class import organization 

class TestEventClass(unittest.TestCase):

    def setUp(self):
        # Create an instance of event for testing
        self.organizaion = organization(
            name = "Test Name",
            email = "Test@mail.utoronto.ca",
            description = "Test Description",
            organization_type = "Test Type"    
        )

    def test_to_dict(self):
        event_dict = self.organizaion.to_dict()
        self.assertIsInstance(event_dict, dict)             #is a dict
        self.assertEqual(event_dict["name"], "Test Name")  #verifies the value to each pair is correct
        self.assertEqual(event_dict["email"], "Test@mail.utoronto.ca")
        self.assertEqual(event_dict["description"], "Test Description")
        self.assertEqual(event_dict["type"], "Test Type")
       
        
    def test_change_name(self):
        self.organizaion.change_name("New organization Name")
        self.assertEqual(self.organizaion.get_name(), "New organization Name")

    def test_add_contact(self):
        new_contacts = [("Paul", "paul123@mail.utoronto.ca"), ("George", "george345@mail.utoronto.ca")]
        self.organizaion.add_contact(new_contacts)
        self.assertEqual(self.organizaion.get_contacts(), new_contacts)



if __name__ == '__main__':
    unittest.main()