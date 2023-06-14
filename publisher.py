from handlers.redis_client import redis_client
import requests
from bs4 import BeautifulSoup
import time

def get_data():
    response = requests.get('https://icanhazdadjoke.com/')
    page = BeautifulSoup(response.text, 'html.parser')
    jokes = page.find('p', {'class': 'subtitle'})

    return [joke.string for joke in jokes if joke.string is not None]

while True:
    time.sleep(5)
    message = str(get_data())
    redis_client.publish('test-channel', message)