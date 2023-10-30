class user:
    #constructor
    def __init__(self, firstname, lastname, email, phone, userID, orgID, orgRole):
        self.firstname = firstname 
        self.lastname = lastname
        self.email = email
        self.phone = phone
        #index for the user database, should use this to access authorization database (password, confidential, etc.), default set to 0 if userID not determined (SQL indices start at 1)
        if userID is None:
            self.userID = 0
        else:
            self.userID = userID 
        #index for the organization database, default set to 0 for no organization (SQL indices start at 1)
        if orgID is None:
            self.orgID = 0
        else:
            self.orgID = orgID 
        #role in the organization. Might be unnecessary if we can just use the orgID and userID to get the role from the organization/user relational database
        if orgRole is None:
            self.orgRole = "None"
        else:
            self.orgRole = orgRole 

    #accessor/mutator methods with likely use cases/reasoning

    #converts all user class fields to a dictionary for easy access to all info. (input for database, profile page, etc.)
    def dictionary(self):
        return {'firstname': self.firstname, 'lastname': self.lastname, 'email': self.email, 'phone': self.phone, 'userID': self.userID, 'orgID': self.orgID, 'orgRole': self.orgRole}

    #didn't think there would ever be a case where name, email or phone would need to be changed after they are set during registration but should be easy to add if needed
    
    #dashboard, profile page, registration list
    def get_firstname(self):
        return self.firstname
    
    #dashboard, profile page, registration list
    def get_lastname(self):
        return self.lastname
    
    #login authorization, notifications
    def get_email(self): 
        return self.email
    
    #notifications
    def get_phone(self):
        return self.phone
    
    #login authorization, event registration/creation, messaging, accessing user database
    def get_userID(self):
        return self.userID
    
    #setting userID for user registration (ID must be unique, prob need to find last ID in db and increment)
    def set_userID(self, userID):
        self.userID = userID
    
    #event creation/management, accessing organization database
    def get_orgID(self):
        return self.orgID
    
    #user registration, joining/leaving organization
    def set_orgID(self, orgID):
        self.orgID = orgID
    
    #organization permissions
    def get_orgRole(self):
        return self.orgRole
    
    #organization management
    def set_orgRole(self, orgRole):
        self.orgRole = orgRole
    
    


