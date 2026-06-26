import psycopg2
from config import DB_CONFIG

def get_connection():
    return psycopg2.connect(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        database=DB_CONFIG["database"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"]
    )

def insert_record(connection, record, topic, partition, offset):
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO social_media_events(
            platform,
            influencer_name,
            account_name,
            category,
            audience_country,
            subscribers,
            avg_views,
            avg_likes,
            avg_comments,
            avg_shares,
            engagement,
            kafka_topic,
            kafka_partition,
            kafka_offset
        )

        VALUES(
            %s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s,
            %s,%s,%s,%s
        )
    """,

    (
        record["platform"],
        record["influencer_name"],
        record["account_name"],
        record["category"],
        record["audience_country"],
        record["subscribers"],
        record["avg_views"],
        record["avg_likes"],
        record["avg_comments"],
        record["avg_shares"],
        record["engagement"],
        topic,
        partition,
        offset
    ))

    connection.commit()
    cursor.close()