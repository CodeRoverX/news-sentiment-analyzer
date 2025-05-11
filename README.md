# 📰 News Sentiment Analyzer

A Python + Streamlit-based app that fetches the latest news headlines based on a keyword and performs sentiment analysis using Hugging Face's `distilBERT` model.

---

## 🔧 Features

- ✅ Fetches top headlines using NewsAPI
- ✅ Preprocesses and cleans the text
- ✅ Analyzes sentiment (Positive / Negative) using `transformers` pipeline
- ✅ Displays confidence score for each prediction
- ✅ Streamlit web interface for user interaction
- ✅ Optionally filters news from the **last 48 hours**

---

## 📦 Tech Stack

- Python 3.8+
- Streamlit
- Hugging Face Transformers
- Requests
- dotenv (.env)
- NewsAPI (https://newsapi.org)

---

## 🚀 How to Run Locally

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/news-sentiment-analyzer.git
cd news-sentiment-analyzer
