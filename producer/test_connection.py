from confluent_kafka import Producer

conf = {
    "bootstrap.servers": "localhost:9092"
}

producer = Producer(conf)

producer.produce(
    "instagram-events",
    key="test",
    value="Hello Kafka!"
)

producer.flush()
    
print("Message sent successfully!")