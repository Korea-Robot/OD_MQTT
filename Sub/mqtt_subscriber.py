# mqtt_subscriber.py
import paho.mqtt.client as mqtt
from config import MQTT_BROKER, MQTT_PORT, MQTT_TOPIC, MQTT_CLIENT_ID, MQTT_USERNAME, MQTT_PASSWORD

# MQTT Broker details
class MQTT_SUB:
    def __init__(self, on_message, username=MQTT_USERNAME, password=MQTT_PASSWORD, qos=1):
        self.client = mqtt.Client(MQTT_CLIENT_ID)
        self.client.username_pw_set(username, password)
        self.qos = qos
        self.client.on_connect = self.on_connect
        self.client.on_message = on_message
        self.client.connect(MQTT_BROKER, MQTT_PORT)
        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        self.client.subscribe(MQTT_TOPIC, self.qos)

    def close(self):
        self.client.loop_stop()
        self.client.disconnect()
