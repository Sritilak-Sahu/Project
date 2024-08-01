import pymongo
try:
    client=pymongo.MongoClient('mongodb://localhost:27017')
    db=client['Mongo-Db']
    collection=db['Mongo-Db project']
    print('Successfull',collection)
   
except Exception as e:
    print("error",e)