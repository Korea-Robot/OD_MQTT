#sang_sub.py
import logging
from sound_player import SoundPlayer
from mqtt_subscriber import MQTT_SUB
from config import DBConfig

if __name__ == '__main__':
    sound_player = SoundPlayer("sus_speech_eng_converted.wav")
    mqtt_sub = MQTT_SUB(sound_player=sound_player)
    mqtt_sub.run()

