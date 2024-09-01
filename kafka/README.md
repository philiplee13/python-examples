## Kafka Example

- docker to bring up kafka topics
- be able to send messages
- be able to consume messages

### Notes

- consumer.py -> listens to messages in a given topic
- producer.py -> publishes messages to a given topic

### Tutorial

https://hackernoon.com/setting-up-kafka-on-docker-for-local-development

- https://kafka-python.readthedocs.io/en/2.0.1/apidoc/modules.html#

### Utills

- kcat (cli util to test kafka): https://github.com/edenhill/kcat
- sample kcat commands
  - list all topics: `kcat -b localhost:9093 -L`
  - to send messages: `kcat -b localhost:9093 -t test-topic -P` (press ctrl + d to send)
  - to listen to messages: `kcat -b localhost:9093 -t test-topic -C`
