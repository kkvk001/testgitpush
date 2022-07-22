import pymongo

client = pymongo.MongoClient("mongodb+srv://kkvk001:kkallen123@cluster0.xffdk.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"sudhanshu",
    "email":"sudhanashu@ineuron.ai",
    "surname":"kumar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)