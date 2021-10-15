



import paho.mqtt.client as mqtt
import time



# create the client
client = mqtt.Client()




client.connect("broker.hivemq.com", 1883)

# subscribe to the topic "my/test/topic"

while True:

# publish "Hello" to the topic "my/test/topic"
   
   client.publish("fan","ON")
   client.publish("led","OFF")
   time.sleep(2)

 