import os
from dotenv import load_dotenv

load_dotenv()

print("KAFKA_BOOTSTRAP_SERVER =", os.getenv("KAFKA_BOOTSTRAP_SERVER"))
print("KAFKA_GROUP_ID =", os.getenv("KAFKA_GROUP_ID"))
print("DB_HOST =", os.getenv("DB_HOST"))

KAFKA_CONFIG = {
    "bootstrap.servers": os.getenv("KAFKA_BOOTSTRAP_SERVER"),
    "group.id": os.getenv("KAFKA_GROUP_ID"),
    "auto.offset.reset": "earliest"
}

TOPICS = [
    "instagram-events",
    "youtube-events",
    "tiktok-events"
]

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD")
}