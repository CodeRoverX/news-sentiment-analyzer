import os 
import requests
import json
from dotenv import load_dotenv

load_dotenv()

ApiKey = os.getenv("NEWSDATA_API_KEY")


def fetch_news_data(query='AI', language='en',country='us', page=1):
    
    
    """
    Fetch news data from the NewsData API.
    
    Args:
        query (str): The search query for the news articles.
        language (str): The language of the news articles.
        page_size (int): The number of articles to fetch.

    Returns:
        list: A list of news articles.
        
    """
    
    url = "https://newsdata.io/api/1/news"
    
    params = {
        'apikey':ApiKey,
        'q':query,
        'language':language,
        # 'country':country,
        # 'page':page
    }
    # if page_size:
    #     params['page_size'] = page_size
    
    
    response = requests.get(url,params=params)
    data = response.json()
    
    if response.status_code !=   200 or 'results' not in data:
        print(f"Error fetching news data: {response.status_code}")
        return []
    
    return data['results']

       
    # url = f"https://newsdata.io/api/1/news?apikey={ApiKey}&q={query}&language={language}&page_size={page_size}"
    # response = requests.get(url)
    
    # if response.status_code == 200:
    #     return response.json().get('results', [])
    # else:
    #     print(f"Error fetching news data: {response.status_code}")
    #     return []

# Example usage:    
# news_data = fetch_news_data(query='AI', language='en', page_size=5)
# print(news_data)
# Uncomment the following lines to test the function
# if __name__ == "__main__":
#     news_data = fetch_news_data(query='AI', language='en', page_size=5)
#     print(json.dumps(news_data, indent=4))
    # Uncomment the following lines to test the function            
    
