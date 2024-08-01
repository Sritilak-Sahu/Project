import pymongo
try:
    client=pymongo.MongoClient('mongodb://localhost:27017')
    db=client['project']
    collection=db['project1']
    # print('Successfull',collection)
    
except Exception as e:
    print("error",e)

def create(name,age,city):
    # db_insert=collection.({'name':name,'age':age,'city':city})
    # print(db_insert,'Successful')
    db_insert=collection.insert_one({'name':name,'age':age,'city':city})
    print(db_insert,'Successful')


def main():
    create('Jio',21,'Rourkela')

main()