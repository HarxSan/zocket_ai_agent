# Web Content Analyzer

![Web Content Analyzer](https://img.shields.io/badge/App-Web%20Content%20Analyzer-blue)
![Python](https://img.shields.io/badge/Python-3.10-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-red)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)

A powerful web application to scrape websites, search the web, and generate AI-powered summaries using Google's Gemini API.

## 🌟 Features

- **Web Scraping**: Extract text content from any website
- **Web Search**: Perform real-time web searches
- **AI Summarization**: Generate concise summaries of content with Gemini AI
- **User-Friendly Interface**: Clean, intuitive Streamlit UI
- **Docker Ready**: Easy deployment with containerization

## 📋 Prerequisites

- Python 3.10 or higher
- Docker (optional, for containerized deployment)
- Jina AI API key
- Google Gemini API key

## 🚀 Quick Start

### Option 1: Run with Python

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/web-content-analyzer.git
   cd web-content-analyzer
   ```

2. **Create an environment file**
   ```bash
   # Create .env file with your API keys
   echo "jina=your_jina_api_key" > .env
   echo "gemini=your_gemini_api_key" >> .env
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Access the app**
   - Open your browser and go to http://localhost:8501

### Option 2: Run with Docker

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/web-content-analyzer.git
   cd web-content-analyzer
   ```

2. **Create an environment file**
   ```bash
   # Create .env file with your API keys
   echo "jina=your_jina_api_key" > .env
   echo "gemini=your_gemini_api_key" >> .env
   ```

3. **Build and run the Docker container**
   ```bash
   docker build -t web-content-analyzer .
   docker run -p 8501:8501 web-content-analyzer
   ```

4. **Access the app**
   - Open your browser and go to http://localhost:8501

## 📱 How to Use

### Web Scraping

1. Click on the "Web Scraping" tab
2. Enter a URL in the input field
3. Click "Scrape Content"
4. View the extracted content and the AI-generated summary

### Web Search

1. Click on the "Web Search" tab
2. Enter your search query
3. Click "Search"
4. View the search results and the AI-generated summary

## 🔧 Configuration

You can provide API keys in three ways:
- Through a `.env` file (recommended for development)
- Through the UI (input fields in the sidebar)
- Through environment variables (for production/Docker)

## 📁 Project Structure

```
web-content-analyzer/
├── app.py              # Main application code
├── Dockerfile          # Docker configuration
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (not committed to git)
└── README.md           # This documentation
```

## 🛠️ Troubleshooting

### Common Issues

1. **Docker build fails:**
   - Make sure Docker is installed and running
   - Check if your requirements.txt file is properly formatted

2. **API errors:**
   - Verify your API keys are correct
   - Check your network connection
   - Ensure the APIs are available and not rate-limited

3. **No content scraped:**
   - Some websites may block scraping
   - Try using a different URL

## 📚 Dependencies

- streamlit: Web application framework
- requests: HTTP library
- python-dotenv: Environment variable management
- google-generativeai: Google's Gemini AI API
- beautifulsoup4: HTML parsing
