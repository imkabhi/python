import pymongo

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb+srv://test:test@cluster0.grlpjvk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Database Name
dataBase = client["labDB"]

# Collection  Name
collection = dataBase['Products']

# Lets Verify all the record at once present in the record with all the fields
all_record = collection.find()

# Printing all records present in the collection
for i in all_record:
     print(i)

print(collection.find_one())

document = collection.find({'name':'Vicky'})

for i in document:
    print(i)