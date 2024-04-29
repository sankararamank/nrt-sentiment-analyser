from confluent_kafka import Producer
from settings import default_config, producer_config


class BaseProducer:
    def publish(self, event):
        pass


class KafkaProducer(BaseProducer):
    def __init__(self):
        self.topic = producer_config["topic"]
        self.producer = Producer(default_config)

    def publish(self, event):
        self.producer.produce(self.topic, value=event)
        self.producer.flush()


class ProducerFactory:
    @staticmethod
    def create():
        if producer_config["type"].upper() == "KAFKA":
            return KafkaProducer()

        raise ValueError("Provider not defined.")
