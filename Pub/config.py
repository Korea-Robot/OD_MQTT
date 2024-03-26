# config.py
class MQTTConfig:
    BROKER = '192.168.168.130'
    PORT = 1883
    TOPIC = 'object_detection/yolo'
    CLIENT_ID = 'object_detector_publisher'
    USERNAME = 'sim'
    PASSWORD = '0604'

class Cam_src:
    URL = 'http://192.168.168.105:8080/stream?topic=/argus/ar0234_front_left/image_raw&quality=40&frame=3'
    PHONE = 1