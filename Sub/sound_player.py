import pygame
from threading import Lock

class SoundPlayer:
    def __init__(self, sound_file):
        self.sound_file = sound_file
        self.sound_lock = Lock()
        pygame.mixer.init()

    def play_sound(self):
        with self.sound_lock:
            try:
                pygame.mixer.music.load(self.sound_file)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
            except Exception as e:
                print(f"Error playing sound: {e}")
