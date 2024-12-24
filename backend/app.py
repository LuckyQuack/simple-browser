from flask import Flask, request, jsonify
from flask_cors import CORS
from summarizer import get_summary_and_keywords

app = Flask(__name__)
CORS(app)

@app.route('/search', methods=['GET'])
def search(): 
    query = request.args.get('query', '').strip()
    if not query:
        return jsonify({'error': 'No query provided'}), 400

    result = get_summary_and_keywords(query)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)