#This is a sample object for event class 
#Demostrates an example instance and the use of certain methods from the class

from datetime import datetime
import event_class


event1_datetime = datetime(2023, 10, 29, 15, 30)
#Initialize and instantiate an obj instance with only the core parameters 
event1 = event_class.event("Coffee_with_Dean", "networking", event1_datetime, "MY330", "Come grab coffee with Christoper Yip and chat!")


#print to terminal
event1.print_all_attributes()


#showing the accessor/mutator methods
event1.set_registration("Reserve your spot on CLNX")
event1.add_accommodation("Coffee and Snacks will be provided")
event1.set_requirement("Open to all students in Engineering!")
event1.size = 70
cohosts = [("Sam", "sam_faculty_member@utoronto.ca"), ("Kyle", "kyle_eng_member@utoronto.ca")]
event1.add_cohost(cohosts)
event1_datetime = event1_datetime.replace(hour=13)
event1.modify_datetime(event1_datetime)

#print
event1.print_all_attributes()

