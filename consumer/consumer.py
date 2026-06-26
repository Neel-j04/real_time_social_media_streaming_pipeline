import json
from confluent_kafka import Consumer
from config import KAFKA_CONFIG, TOPICS
from normalizer import (
    normalize_instagram,
    normalize_youtube,
    normalize_tiktok
)
from database import get_connection, insert_record
from logger import logger

consumer = Consumer(KAFKA_CONFIG)
consumer.subscribe(TOPICS)

print("Listening for Messages...")

logger.info("Kafka Consumer Started")

try:
    connection = get_connection()
    
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue

        if msg.error():
            print(msg.error())
            continue

        data = json.loads(
            msg.value().decode("utf-8")
        )

        topic = msg.topic()

        if topic == "instagram-events":
            record = normalize_instagram(data)

        elif topic == "youtube-events":
            record = normalize_youtube(data)

        else:
            record = normalize_tiktok(data)

        print("=" * 60)
        insert_record(
            connection,
            record,
            msg.topic(),
            msg.partition(),msg.offset()
        )

        logger.info(
            f"{record['platform']} | "
            f"{record['influencer_name']} | "
            f"Inserted Successfully"
        )

        print(
            f"{record['platform']} | "
            f"{record['influencer_name']} | "
            f"Inserted Successfully"
        )

except KeyboardInterrupt:
    logger.info("Consumer Stopped")
    print("\nConsumer Stopped")

finally:
    connection.close()
    consumer.close()