import pymongo
from pymongo import MongoClient
import json

client = MongoClient('mongodb://10.0.0.44:27017/')

db = client.HomeSmartMesh


filename = "boards.json"
collectionname = "boards"

collection = db[collectionname]

with open(filename, 'r') as f:
    post = json.load(f)
post_id = collection.insert_one(post).inserted_id

print filename,"posted @",post_id
