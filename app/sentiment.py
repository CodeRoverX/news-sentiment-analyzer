from transformers import pipeline

# Load the sentiment analysis model
sentiment_model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text):
    """
    Analyzes the sentiment of a given text or list of texts using a pre-trained model.
    
    Args:
        text (str or list): The text or list of texts to analyze.
        
    Returns:
        list: A list of dictionaries with 'label' and 'score' for each input text.
    """
    if isinstance(text, str):
        # If a single string is passed, return the first dictionary from the result
        result = sentiment_model(text)
        return result[0]
    elif isinstance(text, list):
        # If a list of strings is passed, return a list of dictionaries
        return [sentiment_model(t)[0] for t in text]
    else:
        # Handle invalid input
        return [{'label': 'neutral', 'score': 0.0}]