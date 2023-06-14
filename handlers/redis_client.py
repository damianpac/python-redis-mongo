from config import redis_config
import redis
import sys

def conn():
    try:
        client = redis.StrictRedis(**redis_config)
        ping = client.ping()
        if ping is True:
            return client
    except redis.AuthenticationError:
        print("AuthenticationError")
        sys.exit(1) 

redis_client = conn()