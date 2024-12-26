import requests
import spacy
import nltk
import wikipediaapi
from nltk.corpus import stopwords
import os
from dotenv import load_dotenv
from rake_nltk import Rake

load_dotenv()
nlp = spacy.load("en_core_web_sm")
nltk.download('stopwords')
nltk.download('punkt_tab')
stop_words = set(stopwords.words('english'))
wiki = wikipediaapi.Wikipedia(os.getenv('WIKI_USER_AGENT'), 'en')

def get_summary_and_keywords(query):
    page =wiki.page(query)
    if not page.exists():
        return {"title": query, "answer": "No information found for the query.", "keywords": []}

    full_summary = page.summary

    truncated_summary = full_summary[:500]
    if '.' in truncated_summary:
        last_period_index = truncated_summary.rfind('.')
        truncated_summary = truncated_summary[:last_period_index + 1]
    else:
        truncated_summary = truncated_summary.strip()

    keywords = generate_keywords(truncated_summary)
    return {"title": page.title, "answer": truncated_summary, "keywords": keywords}

def generate_keywords(summary):
    doc = nlp(summary)
    
    spacy_keywords = [
        chunk.text for chunk in doc.noun_chunks
        if len(chunk.text) > 3 and chunk.text.lower() not in stop_words
    ]

    rake = Rake(stopwords=stop_words)
    rake.extract_keywords_from_text(summary)
    rake_keywords = []
    for phrase in rake.get_ranked_phrases_with_scores():
        if isinstance(phrase[1], str):
            rake_keywords.append(phrase[1].lower())

    combined_keywords = set(spacy_keywords + rake_keywords)

    filtered_keywords = [
        keyword for keyword in combined_keywords
        if len(keyword.split()) <= 2  
        and keyword.lower() not in stop_words  
    ]
    
    return list(filtered_keywords)[:5]