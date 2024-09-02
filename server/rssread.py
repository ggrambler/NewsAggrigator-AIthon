from flask import Flask, jsonify, request
import feedparser
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import ollama
import json
import os

# Download the VADER lexicon for sentiment analysis
nltk.download('vader_lexicon')

app = Flask(__name__)

# Bloomberg RSS feed URLs
urls = [
    "https://feeds.bloomberg.com/business/news.rss",
    "https://feeds.bloomberg.com/crypto/news.rss"
]

# Initialize Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Function to perform sentiment analysis
def perform_sentiment_analysis(text):
    sentiment_scores = sia.polarity_scores(text)
    return sentiment_scores

# Function to generate AI summary using Ollama
def generate_ai_summary(article_content):
    try:
        # Use the Ollama client to get a response
        response = ollama.chat(
            model="llama3.1",
            messages=[
                {
                    'role': 'user',
                    'content': f"Summarize the following content:\n\n{article_content} If there is nothing clear to summarize , return the content itself or spcify general mood of the buisness news",
                },
            ]
        )
        
        # Extract the summary text
        summary = response['message']['content'].strip()
        return summary or "No summary generated."

    except Exception as e:
        print(f"Error generating AI summary: {e}")
        return "Error generating AI summary."

# Function to fetch live articles from RSS feeds
def fetch_live_articles():
    live_articles = []
    maxart = 3
    for url in urls:
        feed = feedparser.parse(url)
        if feed.entries:
            for art in feed.entries[:maxart]:
                art_values = {}
                # Fetching basic details
                details = ['title', 'summary', 'link', 'published', 'author']
                for detail in details:
                    art_values[detail] = art.get(detail, "N/A")

                # Safely handle 'media_thumbnail' and 'content'
                art_values['thumbnail_url'] = art.get('media_thumbnail', [{}])[0].get('url', "N/A") if 'media_thumbnail' in art else "N/A"
                art_values['content_value'] = art.get('content', [{}])[0].get('value', "N/A") if 'content' in art else "N/A"
                
                # Perform sentiment analysis
                art_values['sentiment'] = perform_sentiment_analysis(art_values['summary'])

                # Generate AI summary using Ollama
                art_values['ai_summary'] = generate_ai_summary(art_values['content_value'])

                # Append article details to the list
                live_articles.append(art_values)

    # Ensure the directory exists
    directory = "C:/Users/Divyansh/Desktop/news aggregator/data"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Save the articles to the text file
    with open(os.path.join(directory, 'articles.txt'), 'w') as file:
        json.dump(live_articles, file)
    
    return live_articles

# API endpoint to get live articles
@app.route('/api/news', methods=['GET'])
def get_live_articles():
    try:
        with open("C:/Users/Divyansh/Desktop/news aggregator/data/articles.txt", 'r') as file:
            articles = json.load(file)
        return jsonify(articles)
    except FileNotFoundError:
        return jsonify({'message': 'No articles found. Please refresh.'}), 404

# API endpoint to refresh the articles data
@app.route('/api/refresh', methods=['POST'])
def refresh_articles():
    articles = fetch_live_articles()
    return jsonify({'message': 'Articles refreshed successfully!', 'articles': articles})

if __name__ == '__main__':
    # Fetch articles when the server starts
    fetch_live_articles()
    app.run(debug=True)
