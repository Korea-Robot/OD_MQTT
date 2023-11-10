# mqtt_subscriber.py
import json
import logging
import paho.mqtt.client as mqtt
from config import MQTTConfig
from threading import Thread
class MQTT_SUB:
    def __init__(self, db, sound_player, qos=1):
        self.db = db
        self.sound_player = sound_player
        self.client = mqtt.Client(MQTTConfig.CLIENT_ID, clean_session=False)
        self.client.username_pw_set(MQTTConfig.USERNAME, MQTTConfig.PASSWORD)
        self.qos = qos
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(MQTTConfig.BROKER, MQTTConfig.PORT)
        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            logging.info("Connected successfully.")
            self.client.subscribe(MQTTConfig.TOPIC, self.qos)
        else:
            logging.error(f"Failed to connect, return code {rc}\n")
        
    def on_message(self, client, userdata, msg):
        logging.info("Received message on {msg.topic}: {msg.payload.decode('utf-8')}")
        payload_data = json.loads(msg.payload.decode('utf-8'))

        # Database insert operation
        self.db.insert_detection(payload_data)

        # Sound playing logic
        if 'keyboard' in payload_data and not self.sound_player.sound_lock.locked():
            Thread(target=self.sound_player.play_sound).start()
            
    def run(self):
        try:
            while True:
                pass
        except KeyboardInterrupt:
            print("Script interrupted by user")
        finally:
            self.client.disconnect()
            self.db.close()
