import streamlit as st
import json

# Function to read articles from the text file
def read_articles_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            articles = json.load(file)
        return articles
    except FileNotFoundError:
        st.error(f"File not found: {file_path}")
        return []
    except json.JSONDecodeError:
        st.error(f"Error decoding JSON from file: {file_path}")
        return []

# Function to display articles
def display_articles(articles):
    if articles:
        for article in articles:
            st.subheader(article.get('title', 'No Title'))
            st.write(f"**Summary:** {article.get('summary', 'No Summary')}")
            st.write(f"[Read more]({article.get('link', '#')})")
            st.write(f"**Published:** {article.get('published', 'No Date')}")
            st.write(f"**Author:** {article.get('author', 'No Author')}")
            st.image(article.get('thumbnail_url', ''), width=150)
            st.write(f"**Sentiment:** {json.dumps(article.get('sentiment', {}), indent=2)}")
            st.write(f"**AI Summary:** {article.get('ai_summary', 'No AI Summary')}")
            st.write("---")
    else:
        st.write("No articles available.")

# Main Streamlit app
def main():
    st.title("News Aggregator")

    # Define the path to the articles file
    file_path = "C:/Users/Divyansh/Desktop/news aggregator/data/articles.txt"

    # Read articles from the file
    articles = read_articles_from_file(file_path)

    # Display articles
    display_articles(articles)

if __name__ == "__main__":
    main()
