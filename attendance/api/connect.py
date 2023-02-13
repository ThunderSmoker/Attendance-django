from pymongo import MongoClient
import pymongo
import os
from dotenv import load_dotenv
load_dotenv()
client = pymongo.MongoClient(os.getenv("MONGO_URI"))
print(os.getenv("MONGO_URI"))
# Get a reference to the database
db = client["Attendance"]
# Get a reference to a collection
batch = db["batch"]
print(type(db))
student_m = db["students"]

