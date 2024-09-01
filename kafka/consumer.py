from kafka import KafkaConsumer
import json

## consumer.py runs forever listening to messages for the given topic

consumer = KafkaConsumer(
    "posts",
    bootstrap_servers=["localhost:9093"],
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),  # json seralizer
)
# note that this for loop will block forever to wait for the next message
for message in consumer:
    print("there was a message")
    print(message.value)
