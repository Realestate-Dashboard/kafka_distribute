from kafka import KafkaConsumer
from typing import Final, List, Optional
import json


def consumer_optional(topic: Optional[str] = None, bootstrap_server: List[str] = None):
    consumer = KafkaConsumer(topic, bootstrap_servers=bootstrap_server, security_protocol="PLAINTEXT")
    return consumer
        

