import pymongo as py # import mongo
connectString = "mongodb://localhost:27017" # connectionString
client = py.MongoClient(connectString) #connect with mongo

# print(client) # check the connection status
db = client.list_database_names() # show all the db name
# print(db)

selectDB = client.get_database("mscit_A_7")

# print(selectDB)
# createCollection = selectDB.create_collection("pythonDB") # create the collection 
# dropCollection = selectDB.drop_collection("pythonDB") # drop collection 

collectionName = selectDB.get_collection("pythonDB") # select the collection 
iteam1 = {
    "name":"Kishan",
    "age":21,
    "course":"mscit"
    
}
# insertData = collectionName.insert_one(iteam1)
# print(insertData)
showData = collectionName.find() #return array 
for item in showData: # print one by one iteam from array 
    print(item)

# apply condition 
filterData = collectionName.find({"age":21},{"_id":0,"name":1})
for data in  filterData:
    print(data)

#update the record
# updateData = collectionName.update_one({"name":"Kishan"},{"$set":{"age":25}})
#print(updateData)

for i in collectionName.find():
    print(i)
# print(collectionName)

# deleteData = collectionName.delete_one({"name":"Kishan"})
# print(deleteData)