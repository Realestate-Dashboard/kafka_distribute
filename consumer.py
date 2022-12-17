from kafka import KafkaConsumer
from typing import Final, List
import json



BIT_TOPIC_NAME: Final[str] = "trade_bitcoin_total"
bootstrap_server: List[str] = ["kafka1:19091", "kafka2:29092", "kafka3:39093"]
consumer = KafkaConsumer(BIT_TOPIC_NAME, bootstrap_servers=bootstrap_server, security_protocol="PLAINTEXT")

for index in (json.loads(i.value.decode()) for i in consumer):
    print(index)