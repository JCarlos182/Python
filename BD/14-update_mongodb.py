from pymongo import MongoClient

client = MongoClient()

mydb = client.obcblog
mycol = mydb.posts

old_value = {"category": "Automação"}
new_value = {"$set": {"category": "Data Analisis"}}

mycol.update_one(old_value, new_value)

for x in mycol.find():
    print(x)