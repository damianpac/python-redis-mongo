from handlers.redis_client import redis_client
from pymongo import MongoClient

esb = redis_client.pubsub()
esb.psubscribe("*-channel")

for message in esb.listen():
    print(message['data'])
    client = MongoClient('mongodb://0.0.0.0:27017');
    db = client['db1dev2']
    collection = db['jokes'] 
    collection.insert_one({"joke": message['data']})