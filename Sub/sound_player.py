import subprocess
from threading import Lock, Thread
import time

class SoundPlayer:
    def __init__(self, sound_file):
        self.sound_file = sound_file
        self.sound_lock = Lock()

    def play_sound_on_device(self, device):
        command = ["aplay", "-D", device, self.sound_file]
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error playing sound on {device}: {e}")

    def play_sound(self):
        with self.sound_lock:
            devices = ["plughw:0,0", "plughw:1,0"]
            threads = []
            for device in devices:
                # Start a thread for each device
                thread = Thread(target=self.play_sound_on_device, args=(device,))
                thread.start()
                threads.append(thread)
            
            # Wait for all threads to complete
            for thread in threads:
                thread.join()
