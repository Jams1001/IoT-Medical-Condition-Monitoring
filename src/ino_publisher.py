import paho.mqtt.client as paho  		           #mqtt library
import os
import serial, time, json
from datetime import datetime

ser = serial.Serial(port = '/dev/ttyACM0', baudrate=9600, timeout=1) 
print("Connected to MCU")

ACCESS_TOKEN='t8Hez8IY76UMd9N3VhSO'                 #Token of your device
broker="iot.eie.ucr.ac.cr"   			            #host name
port=1883 					                        #data listening port

def on_publish(client,userdata,result):             #create function for callback
    print("data published to thingsboard \n")
    pass
client1= paho.Client("control1")                    #create client object
client1.on_publish = on_publish                     #assign function to callback
client1.username_pw_set(ACCESS_TOKEN)               #access token from thingsboard device
client1.connect(broker,port,keepalive=60)           #establish connection
dict = dict()


while True:
    data = ser.readline().decode('utf-8').replace('\r', "").replace('\n', "")
    data = data.split(',')
    if len(data) >= 2:
        print(data)
        dict["BMP"] = data[0]
        dict["TMP"] = data[1]
        print(dict)
        output = json.dumps(dict)
        ret= client1.publish("v1/devices/me/telemetry",output) #topic-v1/devices/me/telemetry