from utils import fetch_news_data
from preprocess import preprocess_articles
from sentiment import analyze_sentiment

# Fetch raw news data
raw_data = fetch_news_data('AI')
print("Raw Articles:")
print(raw_data)
print("*" * 50)

# Preprocess the articles to clean the titles
cleaned_data = preprocess_articles(raw_data)
print("Cleaned Titles:")
for i, title in enumerate(cleaned_data, 1):
    print(f'{i}: {title}')

print("*" * 50)

# Analyze the sentiment of the cleaned titles
res = analyze_sentiment(cleaned_data)

# Print the sentiment results
print("Sentiment Results")
for i, (title, sentiment) in enumerate(zip(cleaned_data, res), 1):
    print(f'{i}, Title: {title}')
    print(f"   ➤ Sentiment: {sentiment['label']} | Confidence: {sentiment['score']:.2f}")
    print("*" * 50)