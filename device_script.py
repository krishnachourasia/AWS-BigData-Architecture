import csv
import random
import json
import time

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from time import sleep
from datetime import date, datetime


CLIENT_NAME = ""
TOPIC = ""

# Broker path is under AWS IoT > Settings (at the bottom left)
BROKER_PATH = "a2hyr29arhu1ac-ats.iot.us-east-1.amazonaws.com"

ROOT_CA_PATH = './AmazonRootCA1.pem'
PRIVATE_KEY_PATH = './14e764a6a2-private.pem.key'
CERTIFICATE_PATH = './14e764a6a2-certificate.pem.crt'

IoTclient = AWSIoTMQTTClient(CLIENT_NAME)
IoTclient.configureEndpoint(BROKER_PATH, 8883)
IoTclient.configureCredentials(
    ROOT_CA_PATH, 
    PRIVATE_KEY_PATH, 
    CERTIFICATE_PATH
)

# Allow the device to queue infinite messages
IoTclient.configureOfflinePublishQueueing(-1)

# Number of messages to send after a connection returns
IoTclient.configureDrainingFrequency(2)  # 2 requests/second

# How long to wait for a [dis]connection to complete (in seconds)
IoTclient.configureConnectDisconnectTimeout(10)

# How long to wait for publish/[un]subscribe (in seconds)
IoTclient.configureMQTTOperationTimeout(5) 


IoTclient.connect()
IoTclient.publish(TOPIC, "connected", 0)

with open('seattle-weather.csv', newline='') as csvfile:
    csv.reader(csvfile, delimiter=',', quotechar='"')
    next(csvfile)
    for row in csvfile:
        time.sleep(2)
        data = row.split(',')
        i=0
        while i < len(data):
            data[i]=data[i].replace('"','')
            data[i]=data[i].replace('\n','')
            i=i+1
        payload = json.dumps({

            "chest x": data[0],
            "chest y": data[1],
            "chest z": data[3],
            "cardio lead1": data[4],
            "cardio lead2": data[5],
            "left ankle x": data[6],
            "left ankle y": data[7],
            "left ankle z": data[8]
        })
        IoTclient.publish(TOPIC, payload, 0)
