from kafka import KafkaConsumer
consumer = KafkaConsumer('testTopic')
for msg in consumer:
	print (msg.value)


"Brendan Cordova","@version":"1"}
[2022-11-22T22:16:33,049][WARN ][logstash.outputs.elasticsearch][main][d921a75d794297f64efc42e9e7968e22180100544ed3fccbd4269edad09e6ed0] 
Could not index event to Elasticsearch. status: 404, action: ["index", {:_id=>nil, :_index=>"testTopic", :routing=>nil}, {"@timestamp"=>2022-11-22T16:46:32.941457800Z, "address"=>"1408 James Ridge\nBrandonborough, AS 16526", "created_at"=>"1987", "event"=>{"original"=>"{\"name\": \"Brendan Cordova\", \"address\": \"1408 James Ridge\\nBrandonborough, AS 16526\", \"
created_at\": \"1987\"}"}, "name"=>"Brendan Cordova", "@version"=>"1"}], response: {"index"=>{"_index"=>"testTopic", "_id"=>nil, "status"=>404, "error"=>{"type"=>"index_not_found_exception", "reason"=>"no such index [testTopic] and [action.auto_create_index] ([.monitoring*,.watches,.triggered_watches,.watcher-history*,.ml*]) doesn't match", "index_uuid"=>"_na_", "index"=>"testTopic"}}}