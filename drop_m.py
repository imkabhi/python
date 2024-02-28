import pymongo

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb+srv://test:test@cluster0.grlpjvk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Database Name
dataBase = client["labDB"]

# Collection  Name
collection = dataBase['Products']

collection.drop()