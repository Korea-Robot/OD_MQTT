import psycopg2
import json
from config import DBConfig

class Database:
    def __init__(self, config=DBConfig):
        self.conn = psycopg2.connect(
            dbname=config.DB_NAME,
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST
        )
        self.cursor = self.conn.cursor()

    def insert_detection(self, payload):
        try:
            # Ensure payload is a JSON formatted string
            if not isinstance(payload, str):
                payload = json.dumps(payload)
            self.cursor.execute("INSERT INTO detections (data) VALUES (%s)", (payload,))
            self.conn.commit()
        except Exception as e:
            print(f"Database insertion failed: {e}")
            self.conn.rollback()

    def close(self):
        self.cursor.close()
        self.conn.close()
