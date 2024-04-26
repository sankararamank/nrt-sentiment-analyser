# nrt-sentiment-analyser

The motivation of this project is to develop a plug and play model to perform sentiment analysis using Kafka and nltk python module. Producers are responsible to transform the ingested data formats such as audio, video etc into text format. This text will be published to a Kafka topic. This app will then consume the message and perform a sentiment analysis in near real time by leveraging the kafka stream behaviour using Faust.

## Setup

1. `pip install requirements.txt`
2. Open the python terminal and do the following
    1. `import nltk`
    2. `nltk.download('all')`
