import psycopg2
from config import DB_NAME, DB_USER, DB_PASS, DB_HOST

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
        self.cursor = self.conn.cursor()

    def insert_detection(self, payload):
        try:
            self.cursor.execute("INSERT INTO detections (data) VALUES (%s)", (json.dumps(payload),))
            self.conn.commit()
        except Exception as e:
            print(f"Database insertion failed: {e}")
            self.conn.rollback()

    def close(self):
        self.cursor.close()
        self.conn.close()
