import json
from fastapi import FastAPI

app = FastAPI()

scrapedData = {}

with open('scrapedDatabase/scrapedData.json', 'r') as file:
    scrapedData = json.load(file)

@app.get("/search")
def search(q: str):
    with open('scrapedDatabase/scrapedData.json', 'r') as file:
        scrapedData = json.load(file)

    keywords = q.lower().split(" ")

    urlsFound = []

    for keyword in keywords:
        if keyword not in scrapedData:
            continue

        urlsFound = urlsFound + scrapedData[keyword]

    return urlsFound
