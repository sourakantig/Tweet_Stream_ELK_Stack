from kafka import KafkaProducer
import json
from faker import Faker
import time



fake=Faker()
def reg_data():

	return{
	'name':fake.name(),
	'address': fake.address(),
	'created_at': fake.year()
	}	
	

def json_ser(data):
	return json.dumps(data).encode('utf-8')


producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=json_ser)


if __name__ == "__main__":
	for _ in range(100):
		red = reg_data()
		print(red)
		producer.send('testTopic', red)
		time.sleep(3)

		