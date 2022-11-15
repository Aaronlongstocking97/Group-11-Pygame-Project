import pymongo
from pymongo import MongoClient
# from datetime import time

cluster = MongoClient(
    "mongodb+srv://AoiKuriki:cse310@escaperoom.5fxfckb.mongodb.net/?retryWrites=true&w=majority")
db = cluster["EscapeRoom"]
score_collection = db["Score"]

# exampleScoreTime = time(second=30, minute=20)

test_score = {"username": "firstName lastname", "score time": "30:00"}

score_collection.insert_one(test_score)

results = score_collection.find()

for result in results:
    print("name:"+result["username"]+","+result["score time"])
