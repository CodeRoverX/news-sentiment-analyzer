from utils import fetch_news_data

news = fetch_news_data("Artificial Intelligence")

for article in news:
    print(article['title'])
