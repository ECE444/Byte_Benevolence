import unittest
from datetime import datetime
from event_class import event  

class TestEventClass(unittest.TestCase):

    def setUp(self):
        # Create an instance of event for testing
        self.event = event(
            event_name="Test Name",
            event_type="Test Type",
            dateTime=datetime(2023, 10, 21, 10, 30),
            location="Test Location",
            description="Test Description"
        )

    def test_to_dict(self):
        event_dict = self.event.to_dict()
        self.assertIsInstance(event_dict, dict)             #is a dict
        self.assertEqual(event_dict["name"], "Test Name")  #verifies the value to each pair is correct
        self.assertEqual(event_dict["type"], "Test Type")
        self.assertEqual(event_dict["place"], "Test Location")

    def test_set_registration(self):
        self.event.set_registration("Registration Instruction")
        self.assertEqual(self.event.get_registration_details(), "Registration Instruction")

    def test_modify_datetime(self):
        new_time = datetime(2023, 10, 23, 14, 30)
        self.event.modify_datetime(new_time)
        self.assertEqual(self.event.get_datetime(), new_time)

    def test_set_requirement(self):
        self.event.set_requirement("New Requirement")
        self.assertEqual(self.event.get_requirement(), "New Requirement")

    def test_change_name(self):
        self.event.change_name("New Event Name")
        self.assertEqual(self.event.get_name(), "New Event Name")

    def test_change_location(self):
        self.event.change_location("New Location")
        self.assertEqual(self.event.get_location(), "New Location")

    def test_add_accommodation(self):
        self.event.add_accommodation("Things provided")
        self.assertEqual(self.event.get_accommodation(), "Things provided")

    def test_add_cohost(self):
        new_contacts = [("Paul", "paul123@mail.utoronto.ca"), ("George", "george345@mail.utoronto.ca")]
        self.event.add_cohost(new_contacts)
        self.assertEqual(self.event.get_cohost(), new_contacts)

    

if __name__ == '__main__':
    unittest.main()
