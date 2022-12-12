from kafka import KafkaConsumer
from typing import Final
import json



TOPIC_NAME: Final[str] = "TRADEBITCOINTOTAL"
bootstrap_server = ["127.0.0.1:9091", "127.0.0.1:9092", "127.0.0.1:9093"]
consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=bootstrap_server, security_protocol="PLAINTEXT")

for index in (json.loads(i.value.decode()) for i in consumer):
    print(index)