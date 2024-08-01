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
def get(q):
    db_get=collection.find_one(q)
    print(db_get,'Successful')
def update(q,n_q):
    db_update=collection.update_one(q,{'$set':n_q})
    print(db_update,'Successful')
def main():
    create('Jio',21,'Rourkela')
    get({'name':'Jio'})
    update({'name':'Jio'},{'name':'Lulla'})
main()