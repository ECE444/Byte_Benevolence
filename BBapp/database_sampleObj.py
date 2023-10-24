import mysql.connector
from database import Database

db = Database()

print(db.insert_user("Peter", "a@mail.utoronto.ca","1234"))

print(db.get_user("a@mail.utoronto.ca"))

db.delete_user("a@mail.utoronto.ca")

print(db.insert_event("my event 1", "Bytes 1","location a", "01:00"))

print(db.get_event("my event 1", "Bytes 1","location a", "01:00"))

db.delete_event("my event 1", "Bytes 1","location a", "01:00")


print(db.insert_organization("Peter", "a@mail.utoronto.ca","1234"))

print(db.get_organization("Peter"))

db.delete_organization("Peter")

