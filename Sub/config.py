# config.py

# Database connection details
class DBConfig:
    DB_HOST = 'localhost'  
    DB_NAME = 'od_mqtt'    
    DB_USER = 'simsang'    
    DB_PASS = '19940604'

# MQTT connection details
class MQTTConfig:
    BROKER = 'localhost'
    PORT = 1883
    TOPIC = 'object_detection/yolo'
    CLIENT_ID = 'object_detector_subscriber'
    USERNAME = 'sang'
    PASSWORD = '1994'

