import pymongo


def connectDB(host,port):
    # 连接上mongodb
    client = pymongo.MongoClient(host=host, port=port)
    # 指定数据库
    db = client.test
    # 指定集合(表)
    collection = db.students
    return collection


def insert(collection,data):
    # 保持数据到mongodb中
    #在 MongoDB 中，每条数据其实都有一个 _id 属性来唯一标识，如果没有显式指明 _id，
    # MongoDB 会自动产生一个 ObjectId 类型的 _id 属性。insert() 方法会在执行后返回的 _id 值
    result = collection.insert(data)#insert方法可以插入多条数据 [{},{}]
    print(result)

def query(collection,condition):
    results = collection.find(condition)
    print(type(results))
    #print(result)
    for result in results:
        print(result)
    pass


if __name__ == '__main__':
    # 数据
    student = {
        'id': '202003',
        'name': 'swy'
    }

    collection = connectDB('192.168.0.103',27017)
    #insert(collection,student)
    #query(collection,{'name' : 'swy'})
    number = collection.find().count()
    print(number)


