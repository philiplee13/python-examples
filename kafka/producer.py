from kafka import KafkaProducer
import json

print("inside producer.py")
producer = KafkaProducer(
    bootstrap_servers=["localhost:9093"],
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)
producer.send("posts", {"test key": "test-value"})
producer.flush()
