#This is a sample object for event class 
#Demostrates an example instance and the use of certain methods from the class

from datetime import datetime
import organization_class


#Initialize and instantiate an obj instance with only the core parameters 
org1 = organization_class.organization("UTRA","UTRA_owner@mail.utoronto.ca","We build Robots!","Design Team")


#print to terminal
org1.print_all_attributes()


#showing the accessor/mutator methods

cohosts = [("Sam", "sam_faculty_member@utoronto.ca"), ("Kyle", "kyle_eng_member@utoronto.ca")]
org1.add_contact(cohosts)

#print
org1.print_all_attributes()