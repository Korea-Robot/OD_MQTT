import logging
from sound_player import SoundPlayer
from mqtt_subscriber import MQTT_SUB
from database import Database
from config import DBConfig

if __name__ == '__main__':
    db = Database(DBConfig)
    sound_player = SoundPlayer("speech_eng.mp3")
    mqtt_sub = MQTT_SUB(db=db, sound_player=sound_player)
    mqtt_sub.run()

