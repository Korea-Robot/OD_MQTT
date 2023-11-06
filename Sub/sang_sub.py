import json
from mqtt_subscriber import MQTT_SUB
from database import Database

# Initialize database
db = Database()

# Callback when a PUBLISH message is received from the server
def on_message(client, userdata, msg):
    print(f"Received message: {msg.topic} {str(msg.payload.decode('utf-8'))}")
    payload_data = json.loads(msg.payload.decode('utf-8'))
    db.insert_detection(payload_data)

# Initialize MQTT client
mqtt_sub = MQTT_SUB(on_message=on_message)
try:
    # Main loop to keep the script running
    while True:
        # The loop can be left empty if your MQTT client library is already handling the loop internally
        pass
except KeyboardInterrupt:
    # Handles the Ctrl-C command which stops the script
    print("Script interrupted by user")
finally:
    # Clean up resources
    mqtt_sub.close()
    db.close()
