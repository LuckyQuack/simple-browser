# Simple Browser

A lightweight web application that provides summarized Wikipedia information with keyword extraction and navigation features. The application consists of a Flask backend and a simple frontend interface.

## Features

- Quick Wikipedia article summaries
- Automatic keyword extraction from summaries
- Clickable keywords for related searches
- Search history navigation
- Clean, minimalist interface

## Prerequisites

- Python 3.7+
- Node.js (for local development)
- pip (Python package manager)

## Required Python Packages

- Flask
- Flask-CORS
- spaCy
- NLTK
- wikipedia-api
- python-dotenv
- rake-nltk

## Installation

1. Clone the repository:
```bash
git clone [your-repository-url]
cd simple-browser
```

2. Install Python dependencies:
```bash
pip install flask flask-cors spacy nltk wikipedia-api python-dotenv rake-nltk
```

3. Download required spaCy model:
```bash
python -m spacy download en_core_web_sm
```

4. Create a `.env` file in the root directory and add your Wikipedia user agent:
```
WIKI_USER_AGENT=your-user-agent-name
```

## Project Structure

```
simple-browser/
├── backend/
│   ├── app.py
│   └── summarizer.py
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
└── README.md
```

## Running the Application

1. Start the Flask backend:
```bash
python app.py
```
The server will start on `http://127.0.0.1:5000`

2. Open `index.html` in your web browser
   - You can use a local server (e.g., Python's `http.server` or VS Code's Live Server)
   - Or open the file directly in your browser

## How It Works

### Backend

- `app.py`: Handles HTTP requests and serves as the API endpoint
- `summarizer.py`: Contains the logic for:
  - Wikipedia article retrieval
  - Text summarization
  - Keyword extraction using spaCy and RAKE algorithms

### Frontend

- Simple interface with search bar and navigation buttons
- Displays article summaries and clickable keywords
- Maintains search history for backward navigation

## API Endpoints

### GET /search
- Parameters:
  - `query` (string): Search term to look up
- Returns:
  - JSON object containing:
    - `title`: Article title
    - `answer`: Summarized content (up to 500 characters)
    - `keywords`: Array of relevant keywords

## Features in Detail

### Summary Generation
- Retrieves Wikipedia article summaries
- Truncates to 500 characters
- Ensures complete sentences by finding the last period

### Keyword Extraction
- Uses both spaCy and RAKE algorithms
- Filters out common stop words
- Limits keywords to 1-2 words
- Returns top 5 most relevant keywords

### Search History
- Maintains history of searches
- Allows navigation to previous searches
- Prevents duplicate consecutive entries

