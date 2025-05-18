import os
from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()

mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri)


db = client["salaryDB"]
collection = db["salaryData"]

if __name__ == "__main__":
    print("Bağlantı başarılı:", db.list_collection_names())