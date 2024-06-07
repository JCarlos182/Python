from pymongo import MongoClient
from pprint import pprint

client = MongoClient()

mydb = client.obcblog
mycol = mydb.posts

result = mycol.find()

for r  in result:
    pprint(r)
    