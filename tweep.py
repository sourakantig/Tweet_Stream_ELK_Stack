import tweepy

#from kafka import KafkaProducer

import json

import cfg

import time



client = tweepy.Client(cfg.bearer_token)



#def json_ser(data):

#	return json.dumps(data).encode('utf-8')



for tweet in tweepy.Paginator(client.search_recent_tweets, query='crypto', max_results=100).flatten(limit = 250):

	print(json.dumps(tweet))

	time.sleep(3)

#producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=json_ser)







#for tweet in tweets:

#	print(tweet.json)

	#producer.send('testTopic', json.dumps(tweet))

#	print("*"*50)

#	time.sleep(3)

