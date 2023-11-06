# mqtt_subscriber.py
import paho.mqtt.client as mqtt
from config import MQTTConfig

class MQTT_SUB:
    def __init__(self, on_message, qos=1):
        self.client = mqtt.Client(MQTTConfig.CLIENT_ID)
        self.client.username_pw_set(MQTTConfig.USERNAME, MQTTConfig.PASSWORD)
        self.qos = qos
        self.client.on_connect = self.on_connect
        self.client.on_message = on_message
        self.client.connect(MQTTConfig.BROKER, MQTTConfig.PORT)
        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected successfully.")
            self.client.subscribe(MQTTConfig.TOPIC, self.qos)
        else:
            print(f"Failed to connect, return code {rc}\n")

    def close(self):
        self.client.loop_stop()
        self.client.disconnect()
