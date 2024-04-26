# Consumes texts to perform sentinment analysis
# Credits: Data Camp
# Ref: https://www.datacamp.com/tutorial/text-analytics-beginners-nltk

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import pandas as pd


# initialize NLTK sentiment analyzer
analyzer = SentimentIntensityAnalyzer()


def _preprocess_text(text):
    # Tokenize the text. Tokens are basically words.
    tokens = word_tokenize(text.lower())

    # Remove stop words
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]

    # Lemmatize the tokens - Brings tokens to their root form
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

    # Join the tokens back into a string
    processed_text = ' '.join(lemmatized_tokens)
    return processed_text


def _get_sentiment(text):
    scores = analyzer.polarity_scores(text)
    sentiment = 1 if scores['pos'] > 0 else 0
    return sentiment


def analyser(data):
    # Load data
    df = pd.read_csv('https://raw.githubusercontent.com/pycaret/pycaret/master/datasets/amazon.csv')

    # Transform using preprocessor
    df['reviewText'] = df['reviewText'].apply(_preprocess_text)

    # Calculate sentiments
    df['sentiment'] = df['reviewText'].apply(_get_sentiment)
    return df
