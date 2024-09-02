// script.js

// Function to fetch articles from the backend and display them on the webpage
async function fetchArticles() {
    try {
        // Fetch data from the Flask server
        const response = await fetch('http://127.0.0.1:5000/api/news');

        // Check if the response is OK
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        // Parse the response JSON
        const articles = await response.json();

        // Display the articles
        displayArticles(articles);
    } catch (error) {
        console.error('Error fetching articles:', error);
    }
}

// Function to display articles on the page
function displayArticles(articles) {
    // Select the container to display articles
    const articlesContainer = document.getElementById('articles-container');
// script.js

// Function to fetch articles from the backend and display them on the webpage
async function fetchArticles() {
    try {
        // Fetch data from the Flask server
        const response = await fetch('http://127.0.0.1:5000/api/news');

        // Check if the response is OK
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        // Parse the response JSON
        const articles = await response.json();

        // Display the articles
        displayArticles(articles);
    } catch (error) {
        console.error('Error fetching articles:', error);
    }
}

// Function to display articles on the page
function displayArticles(articles) {
    // Select the container to display articles
    const articlesContainer = document.getElementById('articles-container');

    // Clear previous articles if any
    articlesContainer.innerHTML = '';

    // Iterate over each article and create HTML elements to display
    articles.forEach(article => {
        const articleElement = document.createElement('div');
        articleElement.classList.add('article');

        // Create HTML content for each article
        articleElement.innerHTML = `
            <h2>${article.title}</h2>
            <p><strong>Author:</strong> ${article.author}</p>
            <p><strong>Published:</strong> ${article.published}</p>
            <p><strong>Summary:</strong> ${article.summary}</p>
            <p><strong>Sentiment:<// script.js

// Function to fetch articles from the backend and display them on the webpage
async function fetchArticles() {
    try {
        // Fetch data from the Flask server
        const response = await fetch('http://127.0.0.1:5000/api/news');

        // Check if the response is OK
        if (!response.ok) {
            throw new Error(``);
        }

        // Parse the response JSON
        const articles = await response.json();

        // Display the articles
        displayArticles(articles);
    } catch (error) {
        console.error('Error fetching articles:', error);
    }
}

// Function to display articles on the page
function displayArticles(articles) {
    // Select the container to display articles
    const articlesContainer = document.getElementById('articles-container');

    // Clear previous articles if any
    articlesContainer.innerHTML = '';

    // Iterate over each article and create HTML elements to display
    articles.forEach(article => {
        const articleElement = document.createElement('div');
        articleElement.classList.add('article');

        // Create HTML content for each article
        articleElement.innerHTML = `
            <div>
            <h2>${article.title}</h2>
            <p><strong>Author:</strong> ${article.author}</p>
            <p><strong>Published:</strong> ${article.published}</p>
            <p><strong>Summary:</strong> ${article.summary}</p>
            <p><strong>Sentiment:</strong> ${JSON.stringify(article.sentiment)}</p>
            <p><strong>AI Summary:</strong> ${article.ai_summary}</p>
            <a href="${article.link}" target="_blank">Read more</a>
            </div>
        `;

        // Append the article to the container
        articlesContainer.appendChild(articleElement);
    });
}

// Call the function to fetch and display articles when the script loads
fetchArticles();
/strong> ${JSON.stringify(article.sentiment)}</p>
            <p><strong>AI Summary:</strong> ${article.ai_summary}</p>
            <a href="${article.link}" target="_blank">Read more</a>
        `;

        // Append the article to the container
        articlesContainer.appendChild(articleElement);
    });
}

// Call the function to fetch and display articles when the script loads
fetchArticles();

    // Clear previous articles if any
    articlesContainer.innerHTML = '';

    // Iterate over each article and create HTML elements to display
    articles.forEach(article => {
        const articleElement = document.createElement('div');
        articleElement.classList.add('article');

        // Create HTML content for each article
        articleElement.innerHTML = `
            <h2>${article.title}</h2>
            <p><strong>Author:</strong> ${article.author}</p>
            <p><strong>Published:</strong> ${article.published}</p>
            <p><strong>Summary:</strong> ${article.summary}</p>
            <p><strong>Sentiment:</strong> ${JSON.stringify(article.sentiment)}</p>
            <p><strong>AI Summary:</strong> ${article.ai_summary}</p>
            <a href="${article.link}" target="_blank">Read more</a>
        `;

        // Append the article to the container
        articlesContainer.appendChild(articleElement);
    });
}

// Call the function to fetch and display articles when the script loads
fetchArticles();
