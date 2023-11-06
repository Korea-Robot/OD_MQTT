# mqtt_publisher.py
import paho.mqtt.client as mqtt
from config import MQTTConfig

class MQTTPublisher:
    def __init__(self):
        self.client = mqtt.Client(MQTTConfig.CLIENT_ID)
        self.client.username_pw_set(MQTTConfig.USERNAME, MQTTConfig.PASSWORD)
        self.client.on_connect = self.on_connect
        self.client.connect(MQTTConfig.BROKER, MQTTConfig.PORT)
        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    def publish(self, payload):
        self.client.publish(MQTTConfig.TOPIC, payload, qos=1)

    def stop(self):
        self.client.loop_stop()
        self.client.disconnect()