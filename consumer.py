from kafka import KafkaConsumer
from typing import Final, List, Optional
import json


def consumer_optional(topic: Optional[str] = None, bootstrap_server: List[str] = None):
    consumer = KafkaConsumer(topic, bootstrap_servers=bootstrap_server, security_protocol="PLAINTEXT")
    for index in (json.loads(i.value.decode()) for i in consumer):
        print(index)
        

