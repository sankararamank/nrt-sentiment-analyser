from confluent_kafka import Consumer
from settings import default_config, consumer_config


class BaseConsumer:
    def subscribe():
        pass

class KafkaConsumer(BaseConsumer):
    def __init__(self):
        self.topic = consumer_config["topic"]
        self.consumer = Consumer(default_config)

    def subscribe(self):
        self.consumer.subscribe([self.topic])

class ConsumerFactory:
    @staticmethod
    def create():
        if consumer_config["type"].upper == "KAFKA":
            return KafkaConsumer()
        
        raise ValueError("Provider not defined.")