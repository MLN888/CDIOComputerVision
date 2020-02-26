import paho.mqtt.client as mqttClient
import time
import keyboard
 
def on_connect(client, userdata, flags, rc):
 
    if rc == 0:
 
        print("Connected to broker")
 
        global Connected                #Use global variable
        Connected = True                #Signal connection 
 
    else:
 
        print("Connection failed")


Connected = False   #global variable for the state of the connection
 
broker_address= "maqiatto.com"
port = 1883
user = "mads-ln@hotmail.dk"
password = "ev3dev"

i = 1
 
client = mqttClient.Client("Python")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.connect(broker_address, port=port)          #connect to broker
 
client.loop_start()        #start the loop
 
while Connected != True:    #Wait for connection
    time.sleep(0.1)
 
while True:
    try:  # used try so that if user pressed other than the given key error will not be shown
        while (keyboard.is_pressed('q')):  # if key 'q' is pressed 
            if not was_pressed:
                client.publish("mads-ln@hotmail.dk/ev3test","Det virker!")
                print('Message sent!')
                was_pressed = True
        else:
            was_pressed = False

            
    except:
        break  # if user pressed a key other than the given key the loop will break
         

    #client.disconnect()
    #client.loop_stop()

    #client.publish("mads-ln@hotmail.dk/ev3test","Det virker!")