from pymongo import MongoClient
import pymongo
import os
from dotenv import load_dotenv
import urllib
load_dotenv()
uri='mongodb+srv://ThunderSmoker:' + urllib.parse.quote('Pitlawar@2004') + '@attendance.czbusw2.mongodb.net/?retryWrites=true&w=majority'
client = pymongo.MongoClient(os.getenv(""))
print(os.getenv("MONGO_URI"))
# Get a reference to the database
db = client["Attendance"]
# Get a reference to a collection
batch = db["batch"]
print(type(db))
student_m = db["students"]

