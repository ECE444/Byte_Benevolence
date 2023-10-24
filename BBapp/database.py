import mysql.connector
class Database:
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host="sql9.freesqldatabase.com",
        user="sql9655237",
        password="bjjEIeT3tm",
        database = "sql9655237",
        port = "3306"
        )

        self.mycursor = self.mydb.cursor()
    
    def insert_user(self, username, email, password): #enforce unique uoft email
        command = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)" 
        self.mycursor.execute(command,(username,email,password))
        result = self.mycursor.fetchall() #incase later we want to see results
        return result
        
    def insert_event(self, name, organization, location, time):
        command = "INSERT INTO events (name, organization, location, time) VALUES (%s, %s, %s, %s)" 
        self.mycursor.execute(command,(name,organization,location,time))
        result = self.mycursor.fetchall() #incase later we want to see results
        return result

    def insert_organization(self, name, email, password): #enforce unique names
        command = "INSERT INTO organizations (name, email, password) VALUES (%s, %s, %s)" 
        self.mycursor.execute(command,(name,email,password))
        result = self.mycursor.fetchall() #incase later we want to see results
        return result

    def delete_user(self, email): 
        command = "DELETE FROM users WHERE email = %s" 
        self.mycursor.execute(command,(email,))
        self.mydb.commit()
        
    def delete_event(self, name, organization, location, time): #assume events may have same names, eg recurring meetings
        command = "DELETE FROM events WHERE name = %s AND organization = %s AND location = %s AND time = %s" 
        self.mycursor.execute(command,(name,organization,location,time))
        self.mydb.commit()

    def delete_organization(self, name): 
        command = "DELETE FROM organizations WHERE name = %s" 
        self.mycursor.execute(command,(name,))
        self.mydb.commit()

    def get_user(self, email):
        command = "SELECT * FROM users WHERE email = %s" 
        self.mycursor.execute(command,(email,))
        result = self.mycursor.fetchall()
        return result 

    def get_event(self, name, organization, location, time):
        command = "SELECT * FROM events WHERE name = %s AND organization = %s AND location = %s AND time = %s" 
        self.mycursor.execute(command,(name,organization,location,time))
        result = self.mycursor.fetchall()
        return result 

    def get_organization(self, name):
        command = "SELECT * FROM organizations WHERE name = %s" 
        self.mycursor.execute(command,(name,))
        result = self.mycursor.fetchall()
        return result 
    
    

