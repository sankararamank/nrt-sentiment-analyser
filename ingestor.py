from argparse import ArgumentParser, FileType
import json

parser = ArgumentParser()
parser.add_argument("dataset_file", type=FileType("r"))
args = parser.parse_args()
tweets = json.load(args.dataset_file)
for tweet in tweets:
    print(tweet)
    break