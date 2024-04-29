#!/usr/bin/env python
from argparse import ArgumentParser, FileType
from configparser import ConfigParser
from confluent_kafka import Consumer


if __name__ == '__main__':
    # Create Consumer instance
    consumer = Consumer(config)

    # Subscribe to topic
    topic = "Poems"

    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                print("[i] Waiting...")
            elif msg.error():
                print(msg.error())
                print(f"[!] ERROR: {msg.error()}")
            else:
                print("[i] Consumed event from topic {topic}: key = {key:12} value = {value:12}".format(topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()