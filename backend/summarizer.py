import requests
import spacy
import nltk
import wikipediaapi
from nltk.corpus import stopwords
import os
from dotenv import load_dotenv

load_dotenv()
nlp = spacy.load("en_core_web_sm")
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
wiki = wikipediaapi.Wikipedia(os.getenv('WIKI_USER_AGENT'), 'en')

def get_summary_and_keywords(query):
    page =wiki.page(query)
    if not page.exists():
        return {"answer": "No information found for the query.", "keywords": []}

    answer = page.summary[:500]

    keywords = generate_keywords(answer)
    return {"answer": answer, "keywords": keywords}

def generate_keywords(summary):
    doc = nlp(summary)
    
    raw_keywords = [chunk.text for chunk in doc.noun_chunks]

    refined_keywords = [
        keyword for keyword in raw_keywords
        if len(keyword) > 3 and keyword.lower() not in stop_words
    ]

    return list(set(refined_keywords))[:5]