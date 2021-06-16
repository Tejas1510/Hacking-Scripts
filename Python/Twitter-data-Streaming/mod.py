import tweepy
import time
from kafka import KafkaConsumer, KafkaProducer
consumer_key = "dRbebEWASLlPzAI3prM9OBv4i"
consumer_secret = "625WMQtDbywEsI6er8QzAmOC1bX1nUJxWTNwXmJTGdz9bUw6Mv"
access_token = "1355447968292192256-6ta4K9q0dLWkiqaWykGPQe0pX25gxe"
access_token_secret = "IEXsiLYfTKOFuEXkL9x6QHx71G6wZOjcVBpvK1LJbfndk"
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)
from datetime import datetime
def normalize_timestamp(time):
  mytime = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
  return(mytime.strftime("%Y-%m-%d %H:%M:%S"))
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],api_version=(2,0,2))
topic_name = 'dhruv2612'
def get_twitter_data():
  res = api.search("BCCI")
  for i in res:
    record = ''
    record += str(i.user.id_str)
    record = '\n'
    record += str(i.text)
    record += ';\n'
    record += str(normalize_timestamp(str(i.created_at)))
    record += ';' 
    record += str(i.user.followers_count)
    record += ';'
    record += str(i.user.location)
    record += ';'
    record += str(i.favorite_count)
    record += ';'
    record += str(i.retweet_count)
    record += ';'
    producer.send(topic_name, str.encode(record))
get_twitter_data()

def periodic_work(interval):
  while True:
    get_twitter_data()
    time.sleep(interval)

periodic_work(60*0.1) 
