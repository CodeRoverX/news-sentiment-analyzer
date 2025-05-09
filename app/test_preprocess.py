from utils import fetch_news_data
from preprocess import clean_txt, preprocess_articles

raw_articles = fetch_news_data('AI')
print("Raw Articles:")
print(raw_articles)

print("*"*50)
cleaned_titles = preprocess_articles(raw_articles)

print("Cleaned Titles:")
for i, title in enumerate(cleaned_titles,1):
    print(f'{i}: {title}')
    
