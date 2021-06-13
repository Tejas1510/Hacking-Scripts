## Twitter Data Streaming
Twitter Data Streaming is a python program 

### About the program
- It's a python program which uses twitter api to retrieve the data of the handle mention by the user.In order to stream the twitter data we have to provide consumer_key,consumer_secret,access_token,access_token_secret which you can get from your developer account.Since you can get the 

### Libraries used
- tweepy
- KafkaConsumer, KafkaProducer from kafka-python

### How to run?
- First install basic modules which are used to run the program [tweepy, kafka, kafka-python]
- Go to twitter Developer and generate the keys [consumer_key,consumer_secret,access_token,access_token_secret]
- copy the keys and paste in the code
- after doing the required changes,You have to install kafka first.
- After Installing Kafka ,run the zookeeper by using the command 'zookeeper-server-start.sh ./config/zookeeper.properties' 
- Then start the kafka by using the command 'kafka-server-start.sh ./config/server.properties' 
  (Run the above two command where you download and install kafka)
- Then run the python script by using command 'python mod.py'
- Then run the command 'kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic dhruv2612 --from-beginning' (run this command where kafka file is set)

### Setup instructions
2. Download this repository as zip and extract
3. Use Python IDLE to run the program.
4. Run the code and stream the twitter data.<br>


### Output
![](https://github.com/dhruv-varshney/Hacking-Scripts/blob/main/Python/Twitter-Data-Streaming/output_images/output1.jpeg)
![](https://github.com/dhruv-varshney/Hacking-Scripts/blob/main/Python/Twitter-Data-Streaming/output_images/output2.jpeg)

After Running this project we not only get the time and text of the tweet,but also we can access the location of almost all the tweets which uses @BCCI


