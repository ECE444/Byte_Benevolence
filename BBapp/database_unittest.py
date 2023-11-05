import unittest
from datetime import datetime
from database import Database  

class TestEventClass(unittest.TestCase):

    def setUp(self):
        # Create an instance of event for testing
        self.database = Database()

    def test_connection(self):
        command = "SHOW DATABASES"
        self.database.mycursor.execute(command)
        self.assertEqual(list(self.database.mycursor)[1][0],'sql9655237')

    def test_basic_functions_users(self):
        #insertion:
        results = self.database.insert_user("Peter", "a@mail.utoronto.ca","1234")
        self.database.mycursor.execute('SELECT last_insert_id() from users')
        batch_id = list(self.database.mycursor)[0][0]

        #get:
        results = self.database.get_user("a@mail.utoronto.ca")
        self.assertEqual(results[-1],('Peter', 'a@mail.utoronto.ca', '1234', batch_id))

        """
        command = "ALTER TABLE users AUTO_INCREMENT = %s" #reset id counter
        self.database.mycursor.execute(command,(batch_id,))
        """

        #delete:
        results = self.database.delete_user("a@mail.utoronto.ca")

        #get:
        results = self.database.get_user("a@mail.utoronto.ca")
        self.assertEqual(results,[])

    def test_basic_functions_events(self):
        #insertion:
        results = self.database.insert_event('my event 1', 'Bytes 1','location a', '01:00')
        self.database.mycursor.execute('SELECT last_insert_id() from events')
        batch_id = list(self.database.mycursor)[0][0]

        #get:
        results = self.database.get_event('my event 1', 'Bytes 1','location a', '01:00')
        self.assertEqual(results[-1],('my event 1', 'Bytes 1','location a', '01:00', batch_id))

        """
        command = "ALTER TABLE users AUTO_INCREMENT = %s" #reset id counter
        self.database.mycursor.execute(command,(batch_id,))
        """

        #delete:
        results = self.database.delete_event('my event 1', 'Bytes 1','location a', '01:00')

        #get:
        results = self.database.get_event('my event 1', 'Bytes 1','location a', '01:00')
        self.assertEqual(results,[])
    
    def test_basic_functions_organizations(self):
        #insertion:
        results = self.database.insert_organization("Peter", "a@mail.utoronto.ca","1234")
        self.database.mycursor.execute('SELECT last_insert_id() from organizations')
        batch_id = list(self.database.mycursor)[0][0]

        #get:
        results = self.database.get_organization("Peter")
        self.assertEqual(results[-1],('Peter', 'a@mail.utoronto.ca', '1234', batch_id))

        """
        command = "ALTER TABLE users AUTO_INCREMENT = %s" #reset id counter
        self.database.mycursor.execute(command,(batch_id,))
        """

        #delete:
        results = self.database.delete_organization("Peter")

        #get:
        results = self.database.get_organization("Peter")
        self.assertEqual(results,[])



if __name__ == '__main__':
    unittest.main()