class user:
    #constructor
    def __init__(self, firstname, lastname, email, phone, userID , orgID, orgRole):
        self.name = firstname 
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.userID = userID #index for the user database, will use this to access authorization database (password, confidential, etc.)
        self.orgID = orgID #index for the organization database
        self.orgRole = orgRole #role type for the organization this might be unnecessary if we can just use the orgID to get the role type from the organization/user relational database

