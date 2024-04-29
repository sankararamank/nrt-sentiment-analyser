from argparse import ArgumentParser, FileType
from configparser import ConfigParser
from confluent_kafka import Producer
# import keyboard

parser = ArgumentParser()
parser.add_argument("config_file", type=FileType("r"))
args = parser.parse_args()

# Parse the configuration.
config_parser = ConfigParser()
config_parser.read_file(args.config_file)
config = dict(config_parser["default"])
producer_config = dict(config_parser["producer"])
producer = Producer(config)

def publish(message):
    producer.produce(producer_config["topic"], value=message)
    producer.flush()  # Ensure the message is sent immediately

# while True:
#     publish(message)
#     if keyboard.is_pressed("q"):
#         break