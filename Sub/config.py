# config.py

# Database connection details
class DBConfig:
    DB_HOST = 'localhost'
    DB_NAME = 'your_db_name'
    DB_USER = 'your_db_user'
    DB_PASS = 'your_db_password'
    
# MQTT connection details
class MQTTConfig:
    BROKER = 'localhost'
    PORT = 1883
    TOPIC = 'object_detection/yolo'
    CLIENT_ID = 'object_detector_subscriber'
    USERNAME = 'sang'
    PASSWORD = '1994'

