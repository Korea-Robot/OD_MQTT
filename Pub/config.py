# config.py
class MQTTConfig:
    BROKER = 'localhost'
    PORT = 1883
    TOPIC = 'object_detection/yolo'
    CLIENT_ID = 'object_detector_publisher'
    USERNAME = 'sim'
    PASSWORD = '0604'
