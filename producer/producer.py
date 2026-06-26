import argparse
import json
import time
import pandas as pd

from kafka import KafkaProducer

parser = argparse.ArgumentParser()

parser.add_argument(
    "--platform",
    required=True,
    choices=[
        "instagram",
        "youtube",
        "tiktok"
    ]
)

args = parser.parse_args()
platform = args.platform

DATASETS = {
    "instagram":
    r"D:/Projects/Cloud Data Engineer Projects/Project_5_Real_Time_Streaming_Pipeline/data/instagram.csv",

    "youtube":
    r"D:/Projects/Cloud Data Engineer Projects/Project_5_Real_Time_Streaming_Pipeline/data/youtube.csv",

    "tiktok":
    r"D:/Projects/Cloud Data Engineer Projects/Project_5_Real_Time_Streaming_Pipeline/data/tiktok.csv"
}

TOPICS = {
    "instagram":
    "instagram-events",

    "youtube":
    "youtube-events",

    "tiktok":
    "tiktok-events"
}

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v:
    json.dumps(v).encode("utf-8")
)

print(f"\nStreaming {platform} dataset...\n")

df = pd.read_csv(DATASETS[platform])

for index, row in df.iterrows():
    message = row.to_dict()
    producer.send(
        TOPICS[platform],
        value=message
    )

    print(f"Sent Record {index+1}")
    time.sleep(1)

producer.flush()
print("\nStreaming Completed.")