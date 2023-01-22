from kafka import KafkaConsumer
consumer = KafkaConsumer('testTopic')
for msg in consumer:
	print (msg.value)

