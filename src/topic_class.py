import cohere
import pandas as pd
from config import COHERE_API_KEY

def classify_topics(texts, labels):
    co = cohere.Client(COHERE_API_KEY)
    response = co.classify(
        model='multilabel',
        inputs=texts,
        examples=[{'text': example, 'label': label} for example, label in labels],
    )
    topics = [result.predictions for result in response.classifications]
    return topics
