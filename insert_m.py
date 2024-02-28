import pymongo

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb+srv://test:test@cluster0.grlpjvk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Database Name
dataBase = client["labDB"]

# Collection  Name
collection = dataBase['Products']

# Sample data
d = {'companyName': 'pwskills',
     'product': 'Affordable AI',
     'courseOffered': 'NLP Learning with Deployment'}

# Insert above records in the collection
rec = collection.insert_one(d)

data3 = [
  { "name": "Amy", "address": "Apple st 652" },
  { "name": "Hannah", "address": "Mountain 21" },
  { "name": "Michael", "address": "Valley 345" },
  { "name": "Sandy", "address": "Ocean blvd 2" },
  { "name": "Betty", "address": "Green Grass 1" },
  { "name": "Richard", "address": "Sky st 331" },
  { "name": "Susan", "address": "One way 98" },
  { "name": "Vicky", "address": "Yellow Garden 2" },
  { "name": "Ben", "address": "Park Lane 38" },
  { "name": "William", "address": "Central st 954" },
  { "name": "Chuck", "address": "Main Road 989" },
  { "name": "Viola", "address": "Sideway 1633" }
]

rec = collection.insert_many(data3)
