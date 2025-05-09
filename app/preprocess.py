import re

def clean_txt(txt):
    txt = txt.lower()
    if not isinstance(txt, str):
        return ''
    
    txt = re.sub(r"http\S+|www\S+","",txt)
    txt = re.sub(r"[^a-zA-Z0-9.,!?\; ]","",txt)
    txt = re.sub(r"\s+"," ",txt).strip()
    
    return txt
    
def preprocess_articles(articles):
    """
    Takes a list of articles and returns a list of cleaned texts.
    """
    
    cleaned = []
    
    for article in articles:
        title = article.get('title', '')
        # if title:
        cleaned_text = clean_txt(title)
        if cleaned_text:
            cleaned.append(cleaned_text)
            
    return cleaned