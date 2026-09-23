from pymongo import MongoClient

MONGO_URL = "mongodb+srv://:.pprdz9s.mongodb.net/?appName=NEXTURN"

client = MongoClient(MONGO_URL)

db = client["student_tracker_db"]

students_collection = db["students"]
