# Twitter Data Streaming Pipeline

## Tech Stack Used
kafka, python, ELK stack(Elastic, Logstash, Kibana)

## Code Explanation

1. Authentication operations were completed with Tweepy module of Python. You must take keys from Twitter API and puth the values in cfg.py.
2. StreamListener named tweepy.py was create for Twitter Streaming. StreamListener produces data for Kafka Topic named 'testTopic'.
3. Producing data was filtered about including desired topic.
4. Also, it converts streaming data to structured data (.json).
5. The data produced by the StreamListener is then consumed by Logstash
6. The Logstash then pushes the data into Elastic search. From there we can visualize the data with the help of Kibana.


<div align="center">
  <img src="https://github.com/sourakantig/Tweet_Stream_ELK_Stack/blob/main/ELK_STEAMING_ARCHITECTURE.png"><br>
</div>



## Running

1. Create Twitter API account and get the authentication keys to put it in cfg.py. 
2. Start Apache Kafka
```
/bin/kafka-server-start.sh /config/server.properties
```
3. Create the Kafka topic in my casr 'testtopic'.
4. Run [tweepy.py] with Python version 3.
5. Before running Logstash, make sure it is configured to listen form the topic that kaska is producing on and it should push the same data to the port that Elastic
   search is running on.
6. Run Logstash with the mentioned configuration.
```
systemctl start logstash
```
7.Run elastic search and make an index in it for the incoming data.
```
/bin/elasticsearch
```

## NOTE
If you want to make sure if your data is getting published at the given topic the it can be tested by running cons.py and then prod.py
