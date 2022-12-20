from kafka import KafkaConsumer
from typing import Final, List
import json



bootstrap_server: List[str] = ["kafka1:19091", "kafka2:29092", "kafka3:39093"]


def consumer_optional(topic: str, bootstrap_server: List[str] = bootstrap_server):
    consumer = KafkaConsumer(topics=topic, bootstrap_servers=bootstrap_server, security_protocol="PLAINTEXT")
    for index in (json.loads(i.value.decode()) for i in consumer):
        print(index)
        

