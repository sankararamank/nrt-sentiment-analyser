from clients.producer import ProducerFactory
from argparse import ArgumentParser, FileType
import json


if __name__ == "__main__":
    producer = ProducerFactory().create()
    parser = ArgumentParser()
    parser.add_argument("dataset_file", type=FileType("r"))
    args = parser.parse_args()
    tweets = json.load(args.dataset_file)
    for tweet in tweets:
        print(f"[i] Processing tweet: {tweet['id']}")
        is_continue = input(">> Continue processing the tweet event? (Y/n)")
        if is_continue.upper() == "Y":
            event = tweet
            producer.publish(event)
        else:
            break
