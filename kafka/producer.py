from kafka import KafkaProducer
from kafka.errors import kafka_errors
import traceback
import json

def producer_demo():
    # 假设生产的消息为键值对（不是一定要键值对），且序列化方式为json
    producer = KafkaProducer(
        bootstrap_servers=['192.168.1.11:9092'],
        key_serializer=lambda k: json.dumps(k).encode(),
        value_serializer=lambda v: json.dumps(v).encode())
    # 发送三条消息
    for i in range(0, 1000):
        future = producer.send(
            topic='kafka_demo',
            key='count_num',  # 同一个key值，会被送至同一个分区
            value=str(i))
        print("send {}".format(str(i)))
        try:
            result = future.get(timeout=10) # 监控是否发送成功
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            continue
        print(result)
    producer.flush()
    #producer.close()


if __name__ == "__main__":
    producer_demo()
