from pymongo import MongoClient

client = MongoClient()
mydb = client.obcblog
mycol = mydb.posts

post1 = {
    "title": "FastApi",
    "category": "Backend",
    "author": {
        "name": "Figueroa",
        "email": "figueroa@gmail.com"
    }
}

result = mycol.insert_one(post1)
print("Documento incluido com sucesso.")