import paho.mqtt.client as mqttClient
import time
import pynput
#from pynput.keyboard import Key, Listener

#1435mm
 
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

 
client = mqttClient.Client("Python")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.connect(broker_address, port=port)          #connect to broker
 
client.loop_start()        #start the loop
 
while Connected != True:    #Wait for connection
    time.sleep(0.1)

lock = False
portOpen = False

#https://pythonhosted.org/pynput/keyboard.html
def on_press(key):
    #print('{0} pressed'.format(key))
    global lock
    global portOpen

    if key == pynput.keyboard.KeyCode(char='w') and lock == False:
        print("Forwards")
        client.publish("mads-ln@hotmail.dk/ev3test","F")
        lock = True
    
    if key == pynput.keyboard.KeyCode(char='a') and lock == False:
        print("Left")
        client.publish("mads-ln@hotmail.dk/ev3test","L")
        lock = True
    
    if key == pynput.keyboard.KeyCode(char='d') and lock == False:
        print("Right")
        client.publish("mads-ln@hotmail.dk/ev3test","R")
        lock = True
    
    if key == pynput.keyboard.KeyCode(char='s') and lock == False:
        print("Backwards")
        client.publish("mads-ln@hotmail.dk/ev3test","B")
        lock = True

    if key == pynput.keyboard.KeyCode(char='q') and portOpen == False:
        print("Port OPEN")
        client.publish("mads-ln@hotmail.dk/ev3test","PO")
        portOpen = True
    
    if key == pynput.keyboard.KeyCode(char='e') and portOpen == True:
        print("Port CLOSE")
        client.publish("mads-ln@hotmail.dk/ev3test","PC")
        portOpen = False
    
    if key == pynput.keyboard.KeyCode(char='e') and portOpen == True:
        print("Port CLOSE")
        client.publish("mads-ln@hotmail.dk/ev3test","PC")
        portOpen = False

    if key == pynput.keyboard.KeyCode(char='j'):
        print("Pas paa Jakob!")
        client.publish("mads-ln@hotmail.dk/ev3test","J")
        portOpen = False

def on_release(key):
    #print('{0} release'.format(key))
    global lock

    if key == pynput.keyboard.KeyCode(char='w') and lock == True:
        print("Forwards STOP")
        client.publish("mads-ln@hotmail.dk/ev3test","S")
        lock = False

    if key == pynput.keyboard.KeyCode(char='a') and lock == True:
        print("Left STOP")
        client.publish("mads-ln@hotmail.dk/ev3test","S")
        lock = False
    
    if key == pynput.keyboard.KeyCode(char='d') and lock == True:
        print("Right STOP")
        client.publish("mads-ln@hotmail.dk/ev3test","S")
        lock = False
    
    if key == pynput.keyboard.KeyCode(char='s') and lock == True:
        print("Backwards STOP")
        client.publish("mads-ln@hotmail.dk/ev3test","S")
        lock = False

    if key == pynput.keyboard.Key.esc:
        # Stop listener
        return False

lock = False

# Collect events until released
with pynput.keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()