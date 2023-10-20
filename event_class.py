from datetime import datetime 



class event:

#MANDATORY fields: name, type, date/time, place, and details
#These must be provided by user before an event can be created. (Inform user on front end, * for mandatory fields)

    def __init__(self, event_name, event_type, dateTime, location, description, registeration=None, accomendation=None, requirement=None, size=None, additional_contact=None):
        self._name = event_name                  #str
        self.type = event_type                   #str   front-end: maybe have tags for user to select when creating event?
        self._time = dateTime                    #datetime obj
        self._place = location                   #str 
        self.details = description               #str
        self._booking = registeration            #front-end: let user select Y/N. If Y, make them input booking instructions as string. If N, pass reservation as "Not required" or just dont provide it during initialization
        self.accomendation = accomendation       #str
        self._requisite = requirement            #str
        if size is None:
            self.size = "no limit"        
        else:
            self.size = size                         #int 
        if additional_contact is not None:
            self._contact = additional_contact   #additional_contact will be passed as a list of (name, email) pair parsed from user input
        else:
            self._contact = []                   #contacts stored in a list of (string, string) pair 




#Method to convert obj instance into dictionary - may be convenient when working with flask and MongoDB later

    def to_dict(self):

        event_dict = {
           "name": self._name,
           "type": self.type,
           "time": self._time.strftime("%Y-%m-%d %H:%M"),
           "place": self._place,
           "details": self.details,
           "booking": self._booking,              
           "accommodation": self.accommodation,
           "requisite": self._requisite,
           "size": self.size,
           "contact": self._contact           
        }  
       
        return event_dict
    

#Accessor and mutator methods for private members: booking, place, time, contacts, requisite, and name

    def set_registration(self, booking_details):
        self._booking = booking_details

    def get_registration_details(self):
        if(self._booking == None):
            self._booking = "Not required"
        return self._booking

    def modify_datetime(self, new_time):
        self._time = new_time

    def get_datetime(self):
        return self._time

    def set_requirement(self, new_requirement):
        self._requisite = new_requirement

    def get_requirement(self):
        if(self._requisite == None):
            self._requisite = "Everyone is welcome!"
        return self._requisite
    
    def change_name(self, new_name):
        self._name = new_name

    def get_name(self):
        return self._name
    
    def change_location(self, new_location):
        self._place = new_location

    def get_location(self):
        return self._place

    def add_accomendation(self, accomendate):
        self.accomendation = accomendate

    def get_accomendation(self):
        if(self.accomendation == None):
            self.accomendation = "N/A"
        return  self.accomendation

    def add_cohost(self, new_contacts):
        if not isinstance(new_contacts, list):
            raise ValueError("The argument should be a list")

        for pair in new_contacts:
            if not isinstance(pair, tuple) or not all(isinstance(name, str) for name in pair):
                raise ValueError("Should come in a pair of (name, contact_method)")

        self._contact.extend(new_contacts)


    def get_cohost(self):
        if(self._contact == []):
            return "None"
        
        return self._contact


    def print_all_attributes(self):

        if self._contact is not None:
            message = "\n"
            for pair in self._contact:
                message += f"{pair[0]}: {pair[1]}\n"

        if self._contact == []:
            message = " None"

        print("\nEvent name: " + self.get_name() + "\nEvent type: " + self.type + "\nTaking place on: " + self.get_datetime().strftime("%Y-%m-%d %H:%M") + "\nTaking place at: " + self.get_location() + "\nWhat is happening: " + self.details + "\nRegisteration: " + self.get_registration_details() + "\nAccomendations: " + self.get_accomendation() + "\nRequirements: " + self.get_requirement() + "\nEvent Size: " + str(self.size) + "\nCo-Organizers: " + message)



    

