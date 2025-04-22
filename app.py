# app.py
import streamlit as st
import requests
from dotenv import load_dotenv
import os
import google.generativeai as genai
from bs4 import BeautifulSoup

def load_api_keys():
    """Load API keys from .env file or from Streamlit secrets"""
    load_dotenv()
    
    jina_key = os.getenv('jina') or st.secrets.get("jina", "")
    gemini_key = os.getenv('gemini') or st.secrets.get("gemini", "")
    
    return jina_key, gemini_key

def scrape_url(url, api_key):
    """Scrape content from a URL using Jina API"""
    api_url = "https://r.jina.ai"
    headers = {"Authorization": f"Bearer {api_key}"}
    
    try:
        response = requests.get(f"{api_url}/{url}", headers=headers)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            content = soup.get_text() 
            return content, None
        else:
            return None, f"Error: Status code {response.status_code}"
    except Exception as e:
        return None, f"Error: {str(e)}"

def web_search(question, api_key):
    """Perform web search using Jina API"""
    api_url_grounding = "https://s.jina.ai"
    headers = {"Authorization": f"Bearer {api_key}"}
    
    try:
        response = requests.get(f"{api_url_grounding}/{question}", headers=headers)
        
        if response.status_code == 200:
            content = response.text
            return content, None
        else:
            return None, f"Error: Status code {response.status_code}"
    except Exception as e:
        return None, f"Error: {str(e)}"

def summarize_with_gemini(content, api_key):
    """Summarize content using Google's Gemini API"""
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        
        prompt = f"""
        Use the provided content: {content} to summarize the content and extract key points.
        
        Focus on the following aspects:
        1. **Main ideas and themes**: Capture the core message and topics discussed.
        2. **Key facts and data**: Highlight relevant statistics, dates, and notable figures.
        3. **Arguments or opinions**: Identify key arguments, viewpoints, or perspectives.
        4. **Conclusions or recommendations**: Summarize conclusions, suggestions, or actionable items.
        5. **Important quotes or references**: Extract significant quotes, sources, or external references.
        
        Ensure the summary is clear, concise, and organized by aspect. Focus on presenting only the most essential and impactful points.
        """
        
        response = model.generate_content(prompt)
        return response.text, None
    except Exception as e:
        return None, f"Error: {str(e)}"

def main():
    st.set_page_config(
        page_title="Web Content Analyzer",
        page_icon="🔍",
        layout="wide"
    )
    
    st.title("Web Content Analyzer")
    st.write("Scrape websites, search the web, and generate AI summaries.")
    
    # Load API keys
    jina_key, gemini_key = load_api_keys()
    
    # Check if API keys are available
    if not jina_key or not gemini_key:
        st.warning("Please set the API keys in the sidebar.")
    
    with st.sidebar:
        st.header("API Configuration")
        jina_key_input = st.text_input("Jina API Key", value=jina_key, type="password")
        gemini_key_input = st.text_input("Gemini API Key", value=gemini_key, type="password")
        
        if st.button("Save Keys"):
            jina_key = jina_key_input
            gemini_key = gemini_key_input
            st.success("API keys updated!")
    
    tab1, tab2 = st.tabs(["Web Scraping", "Web Search"])
    
    # Web Scraping Tab
    with tab1:
        st.header("Web Content Scraper")
        url_to_scrape = st.text_input("Enter the URL to scrape:")
        
        if st.button("Scrape Content", key="scrape_button"):
            if not url_to_scrape:
                st.error("Please enter a URL.")
            elif not jina_key:
                st.error("Jina API key is missing.")
            else:
                with st.spinner("Scraping content..."):
                    content, error = scrape_url(url_to_scrape, jina_key)
                
                if error:
                    st.error(error)
                elif content:
                    st.success("Content scraped successfully!")
                    
                    # Display raw content in an expandable section
                    with st.expander("View Raw Content"):
                        st.text_area("Extracted Content", content, height=300)
                    
                    if gemini_key:
                        with st.spinner("Generating summary..."):
                            summary, summary_error = summarize_with_gemini(content, gemini_key)
                        
                        if summary_error:
                            st.error(f"Summary generation failed: {summary_error}")
                        else:
                            st.subheader("Content Summary")
                            st.markdown(summary)
                    else:
                        st.warning("Gemini API key is required for summarization.")
                else:
                    st.error("No content was extracted from the URL.")
    
    # Web Search Tab
    with tab2:
        st.header("Web Search")
        search_query = st.text_input("Enter your search query:")
        
        if st.button("Search", key="search_button"):
            if not search_query:
                st.error("Please enter a search query.")
            elif not jina_key:
                st.error("Jina API key is missing.")
            else:
                with st.spinner("Searching..."):
                    search_results, search_error = web_search(search_query, jina_key)
                
                if search_error:
                    st.error(search_error)
                elif search_results:
                    st.success("Search completed!")
                    
                    # Display search results
                    with st.expander("View Search Results"):
                        st.text_area("Results", search_results, height=300)
                    
                    if gemini_key:
                        with st.spinner("Generating summary..."):
                            summary, summary_error = summarize_with_gemini(search_results, gemini_key)
                        
                        if summary_error:
                            st.error(f"Summary generation failed: {summary_error}")
                        else:
                            st.subheader("Search Results Summary")
                            st.markdown(summary)
                    else:
                        st.warning("Gemini API key is required for summarization.")
                else:
                    st.error("No results found.")

if __name__ == "__main__":
    main()