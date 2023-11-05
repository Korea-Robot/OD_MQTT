# mqtt_publisher.py
import paho.mqtt.client as mqtt

# MQTT Broker details
MQTT_BROKER = 'localhost'
MQTT_PORT = 1883
MQTT_TOPIC = 'object_detection/yolo'
CLIENT_ID = 'object_detector'

# Function to connect to MQTT Broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

# Setup MQTT Client
mqtt_client = mqtt.Client(CLIENT_ID)
mqtt_client.on_connect = on_connect
mqtt_client.connect(MQTT_BROKER, MQTT_PORT)
mqtt_client.loop_start()

def publish_to_mqtt(payload):
    mqtt_client.publish(MQTT_TOPIC, payload, qos=1)

def stop_mqtt():
    mqtt_client.loop_stop()
    mqtt_client.disconnect()
