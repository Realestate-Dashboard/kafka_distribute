import time
import json

from typing import Optional
from kafka import KafkaProducer



def producer_optional(producer: KafkaProducer, data: dict, topic: Optional[str]=None):
    producer.send(topic=topic, value=json.dumps(data).encode("utf-8"))
    producer.flush()
    time.sleep(1)
