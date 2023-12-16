from kafka import KafkaConsumer
from kafka.errors import kafka_errors
import traceback
import json

def consumer_demo():
    consumer = KafkaConsumer(
        'kafka_demo',
        bootstrap_servers=['localhost:9092'],
        group_id='test',
        consumer_timeout_ms=1000
    )
    for message in consumer:
        print("receive, key: {}, value: {}".format(
            json.loads(message.key.decode()),
            json.loads(message.value.decode())
            )
        )

    print("hahaha")


if __name__ == "__main__":
    consumer_demo()
