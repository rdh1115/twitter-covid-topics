import cohere
import pandas as pd
from config import COHERE_API_KEY

def analyze_sentiment(texts):
    co = cohere.Client(COHERE_API_KEY)
    response = co.classify(
        model='sentiment',
        inputs=texts,
    )
    sentiments = [result.prediction for result in response.classifications]
    return sentiments

