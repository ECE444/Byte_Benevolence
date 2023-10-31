from datetime import datetime 

class organization:

#MANDATORY fields: name, type, date/time, place, and description
#These must be provided by user before an event can be created. (Inform user on front end, * for mandatory fields)

    def __init__(self, name, email, description, organization_type, additional_contact=None, events=None):
        self._name = name                   #str
        self.email = email                 #str
        self.description = description         #str
        self.type = organization_type      #str   front-end: maybe have tags for user to select when creating event?
        if additional_contact is not None:
            self._contact = additional_contact   #additional_contact will be passed as a list of (name, email) pair parsed from user input
        else:
            self._contact = []                   #contacts stored in a list of (string, string) pair 
        self.events = events                    #list of events. Needs more thinking




#Method to convert obj instance into dictionary - may be convenient when working with flask and MongoDB later

    def to_dict(self):

        event_dict = {
           "name": self._name,
           "email": self.email,
           "type": self.type,
           "description": self.description,
           "contact": self._contact           
        }  

        return event_dict


#Accessor and mutator methods for private members: booking, place, time, contacts, requisite, and name

    def get_email(self):
        return self.email

    def change_name(self, new_name):
        self._name = new_name

    def get_name(self):
        return self._name
    
    def change_description(self, new_desc):
        self.description = new_desc

    def get_description(self):
        return self.description
    
    def change_type(self, new_type):
        self.type = new_type

    def get_type(self):
        return self.type
    
    def add_contact(self, new_contacts):
        if not isinstance(new_contacts, list):
            raise ValueError("The argument should be a list")

        for pair in new_contacts:
            if not isinstance(pair, tuple) or not all(isinstance(name, str) for name in pair):
                raise ValueError("Should come in a pair of (name, contact_method)")

        self._contact.extend(new_contacts)
    
    def get_contacts(self):
        return self._contact


    def print_all_attributes(self):

        if self._contact is not None:
            message = "\n"
            for pair in self._contact:
                message += f"{pair[0]}: {pair[1]}\n"

        if self._contact == []:
            message = " None"

        print("\Organizaion name: " + self.get_name() + "\Organization type: " + self.type + "\nWhat this org is about: " + self.description)
