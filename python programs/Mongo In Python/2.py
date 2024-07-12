import pymongo as py
client = py.MongoClient("mongodb://localhost:27017")
db = client["KB1"]
# collection = db.create_collection("student")
collection = db.get_collection("student")
# name = input("Enter a name :")
# age = input("Enter age :")
# course = input("Enter course :")
# salary = input("Enter salary :")
# data1 = {
#     "name":name,
#     "age":int(age),
#     "course":course,
#     "salary":int(salary)
# }
# insertData = collection.insert_one(data1)
data = collection.find({},{"_id":0})
for i in data:
    print(i)


