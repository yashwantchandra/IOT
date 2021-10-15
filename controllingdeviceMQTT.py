import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
    else:
        print("Connect returned result code: " + str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):

    #code to controll the respberrypi
    print("Received message: " + msg.topic + " -> " + msg.payload.decode("utf-8"))
    if msg.payload.decode("utf-8")== "ON" and msg.topic=="fan":
        print(" Fan is On") 
       
    elif  msg.payload.decode("utf-8")== "OFF" and msg.topic=="fan": 
        print("fan is off")  
        
    elif msg.payload.decode("utf-8")== "ON" and msg.topic=="led":
        print("led is on")  
     
    elif   msg.payload.decode("utf-8")== "OFF" and msg.topic=="led":    
        print("led is OFF")
        

# create the client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message




# connect to HiveMQ Cloud on port 8883
client.connect("broker.hivemq.com",1883)

# subscribe to the topic "my/test/topic"
client.subscribe("fan")
client.subscribe("led")





client.loop_forever()