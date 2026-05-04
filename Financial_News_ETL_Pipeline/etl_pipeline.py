import pandas as pd
import datetime as dt
import torch
from transformers import pipeline

def extract_data():
    print("Extracting mock financial data...")
    mock_news_data = [
        {"title": "Apple announces record-breaking iPhone sales for Q3", "publisher": "Tech Journal", "providerPublishTime": 1714780800},
        {"title": "Supply chain issues cause potential production delays for AAPL", "publisher": "Market Watch", "providerPublishTime": 1714694400},
        {"title": "Apple to invest $1 Billion in new generative AI features", "publisher": "Finance Daily", "providerPublishTime": 1714608000},
        {"title": "Tech stocks tumble as inflation data misses expectations", "publisher": "Wall Street News", "providerPublishTime": 1714521600},
        {"title": "Apple CEO Tim Cook outlines steady growth strategy for next year", "publisher": "Business Insider", "providerPublishTime": 1714435200}
    ]
    df = pd.DataFrame(mock_news_data)[['title', 'publisher', 'providerPublishTime']]
    df['date'] = pd.to_datetime(df['providerPublishTime'], unit='s')
    return df

def transform_data_with_ai(df):
    print("Loading FinBERT AI Model...")
    sentiment_analyzer = pipeline("sentiment-analysis", model="ProsusAI/finbert")
    
    def get_finbert_sentiment(headline):
        try:
            result = sentiment_analyzer(headline)[0]
            return result['label'].upper()
        except Exception:
            return "ERROR"
            
    print("Scoring sentiment...")
    df['ai_sentiment'] = df['title'].apply(get_finbert_sentiment)
    return df

def load_data(df):
    # Standard local save for GitHub demonstration purposes
    file_path = "financial_sentiment_data.csv"
    df.to_csv(file_path, index=False)
    print(f"Pipeline Complete! Data saved to {file_path}")

if __name__ == "__main__":
    raw_data = extract_data()
    transformed_data = transform_data_with_ai(raw_data)
    load_data(transformed_data)