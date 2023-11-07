import json
import pygame
from mqtt_subscriber import MQTT_SUB
from database import Database
from config import DBConfig

# Initialize database
#db = Database(DBConfig)

# Initialize the mixer module
pygame.mixer.init()

# Callback when a PUBLISH message is received from the server
def on_message(client, userdata, msg):
    print(f"Received message on {msg.topic}: {msg.payload.decode('utf-8')}")
    payload_data = json.loads(msg.payload)
    #db.insert_detection(payload_data)
    
    # Check if "keyboard" is in the message and play sound if it is
    if 'keyboard' in payload_data:
        try:
            pygame.mixer.music.load('speech_eng.mp3')  # Replace with your MP3 file path
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():  # Wait for the music to finish playing
                pygame.time.Clock().tick(10)
        except Exception as e:
            print(f"Error playing sound: {e}")

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
    #db.close()
