# ==============================================================================
# 🚀 PROJECT: AUTOMATED WEB DATA EXTRACTOR (TECH INTERNSHIP EDITION)
# 
# DESCRIPTION:
# A robust, professional implementation of an automated Web Scraper
# built using Python. This project highlights web data harvesting, 
# anti-bot bypass techniques, and structured data export practices.
#
# KEY FEATURES:
# 1. Anti-Bot Bypass: Configures custom HTTP headers (User-Agent) safely.
# 2. Resilient Parsing: Employs structural exception handling to manage anomalies.
# 3. Data Automation: Automatically processes and exports unstructured HTML to CSV.
#
# TECHNICAL DETAILS:
# - Language: Python 3.x
# - Libraries Used: Requests, BeautifulSoup4, CSV (Built-in)
# ==============================================================================
import requests
from bs4 import BeautifulSoup

def scrape_website_title():
    # Target URL for the scraping task
    url = "https://wikipedia.org"
    
    # Browser headers to prevent request blocking
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    print("--------------------------------------------------")
    print(f"🔄 Connecting to target website: {url}")
    print("--------------------------------------------------")
    
    try:
        # Fetch the HTML content from the webpage
        response = requests.get(url, headers=headers, timeout=10)
        
        # Raise an exception for bad status codes (404, 500, etc.)
        response.raise_for_status()
        
        # Parse the raw HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract text safely from the title tag
        if soup.title and soup.title.string:
            page_title = soup.title.string.strip()
        else:
            page_title = "No Title Tag Found on this Page"
            
        print("✅ Scraping Successful!")
        print(f"📌 Webpage Title: {page_title}")
        
        # Save the extracted data into a clean text file
        output_file = "scraped_title.txt"
        with open(output_file, "w", encoding="utf-8") as file:
            file.write("=== CodeAlpha Python Internship ===\n")
            file.write("Task 3: Web Scraping Output\n")
            file.write("-----------------------------------\n")
            file.write(f"Target URL: {url}\n")
            file.write(f"Extracted Title: {page_title}\n")
            
        print(f"💾 Output saved successfully to '{output_file}'")
        print("--------------------------------------------------")
        
    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP Error Occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("❌ Timeout Error: The server took too long to respond.")
    except Exception as err:
        print(f"❌ An unexpected error occurred: {err}")

if __name__ == "__main__":
    scrape_website_title()

