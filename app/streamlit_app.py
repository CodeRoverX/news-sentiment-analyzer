import streamlit as st
from utils import fetch_news_data
from preprocess import preprocess_articles
from sentiment import analyze_sentiment

st.title("News Sentiment Analysis")
st.write("This app fetches news articles and analyzes their sentiment.")

# Fetch news data
keywords = st.text_input("Enter keywords to search for news articles (comma-separated):", "AI")

if st.button("Fetch News"):
    with st.spinner("Fetcing news articles..."):
        raw_data = fetch_news_data(keywords)
        
        if not raw_data:
            st.warning("⚠️ No recent news found. Try a different keyword or search for news from the last 48 hours.")

        else:
            cleaned_data = preprocess_articles(raw_data)
            results = analyze_sentiment(cleaned_data)
            # st.success("News articles fetched and analyzed successfully!")
            
            if not results:
                st.warning("⚠️ No articles found for the given keywords.")
            else:
                st.success("News articles fetched and analyzed successfully!")
                st.subheader("Sentiment Analysis Results")
                for i, (title, sentiment) in enumerate(zip(cleaned_data, results), 1):
                    st.markdown(f"**{i}.** {title}")
                    st.write(f"→ Sentiment: {sentiment['label']} | Confidence: {round(sentiment['score'], 2)}")
                    st.markdown("---")