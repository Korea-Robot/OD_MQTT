# main_subscriber.py
import json
from mqtt_subscriber import MQTT_SUB
from database import Database
from config import DBConfig

# Initialize database
db = Database(DBConfig)

# Callback when a PUBLISH message is received from the server
def on_message(client, userdata, msg):
    print(f"Received message on {msg.topic}: {msg.payload.decode('utf-8')}")
    payload_data = json.loads(msg.payload)
    db.insert_detection(payload_data)

# Initialize MQTT client with the defined callback function
mqtt_sub = MQTT_SUB(on_message=on_message)

try:
    # Main loop to keep the script running
    while True:
        pass  # Your MQTT client library handles the loop internally
except KeyboardInterrupt:
    # Handles the Ctrl-C command which stops the script
    print("Script interrupted by user")
finally:
    # Clean up resources
    mqtt_sub.close()
    db.close()
