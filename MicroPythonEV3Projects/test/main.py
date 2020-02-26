#!/usr/bin/env python3

import paho.mqtt.client as mqttClient
from ev3dev2.auto import *
from time import sleep
import os
os.system('setfont Lat15-TerminusBold14')

#####

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("mads-ln@hotmail.dk/ev3test")
  #client.publish("mads-ln@hotmail.dk/ev3test","ev3dev here!")

def on_message(client, userdata, msg):
    #print(msg.payload.decode())
    leds.set_color("LEFT", "RED")
    tank_drive.on_for_rotations(SpeedPercent(100), SpeedPercent(100), 4)


broker_address= "maqiatto.com"
port = 1883
user = "mads-ln@hotmail.dk"
password = "ev3dev"

leds = Leds()
#m = LargeMotor(OUTPUT_A)
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)

client = mqttClient.Client("ev3")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.connect(broker_address, port=port)          #connect to broker

 
client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
