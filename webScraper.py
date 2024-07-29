import requests
import time
import json
from bs4 import BeautifulSoup
import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

scrapedData = {}

with open('scrapedDatabase/scrapedData.json', 'r') as file:
    scrapedData = json.load(file)

visitedURLs = []

def find_topic(sentence):
    # Process the sentence
    doc = nlp(sentence)
    
    # Extract the most relevant noun or noun chunk
    for chunk in doc.noun_chunks:
        return chunk.text

def find_document_topic(soup):
    paragraphs = [a.get_text() for a in soup.find_all('p') if a.get_text()]

    sentence = ' '.join(paragraphs)

    topic = find_topic(sentence)

    return topic

def extract_links(soup):
    # Find all the anchor tags with href attributes
    links = [a['href'] for a in soup.find_all('a', href=True)]

    return links

def scrape(url):
    if url in visitedURLs:
        return

    visitedURLs.append(url)

    with open('scrapedDatabase/visitedURLs.json', 'w') as file:
        json.dump(visitedURLs, file, indent=4)

    try:
        response = requests.get(url, timeout=2)
        response.raise_for_status() # Raise an exception for HTTP errors

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        links = extract_links(soup)

        topics = find_document_topic(soup).lower()

        for topic in topics.split(" "):
            if topic not in scrapedData:
                scrapedData[topic] = []
            
            if url not in scrapedData[topic]:
                scrapedData[topic].append(url)

        with open('scrapedDatabase/scrapedData.json', 'w') as file:
            json.dump(scrapedData, file, indent=4)

        for link in links:
            print(link)
            scrape(link)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return
        
    except Exception as e:
        print(f"Error: {e}")
        return

startingURL = 'https://example.com/'
scrape(startingURL)