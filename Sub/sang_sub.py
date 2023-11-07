import json
from sound_player import SoundPlayer
from mqtt_subscriber import MQTT_SUB
from database import Database
from config import DBConfig
from threading import Thread

# Initialize database
#db = Database(DBConfig)
sound_player = SoundPlayer("speech_eng.mp3")

# Callback when a PUBLISH message is received from the server
def on_message(client, userdata, msg):
    print(f"Received message on {msg.topic}: {msg.payload.decode('utf-8')}")
    payload_data = json.loads(msg.payload)
    # db.insert_detection(payload_data)  # Uncomment if you want to insert into the database
    # Check if "keyboard" is in the message and play sound if it is
    if 'keyboard' in payload_data and not sound_player.sound_lock.locked():
        Thread(target=sound_player.play_sound).start()  # Start the playback in a separate thread

# Initialize database
# db = Database(DBConfig)

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
    # db.close()  # Uncomment if you are using a database