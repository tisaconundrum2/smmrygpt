from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

RAPIDAPI_KEY = 'your_rapidapi_key_here'
RAPIDAPI_HOST = 'article-extractor-and-summarizer.p.rapidapi.com'
BASE_URL = 'https://article-extractor-and-summarizer.p.rapidapi.com/summarize'

headers = {
    'X-RapidAPI-Key': RAPIDAPI_KEY,
    'X-RapidAPI-Host': RAPIDAPI_HOST
}

# Route to handle input directly from the URL
@app.route('/<text>', methods=['GET'])
def summarize_from_url(text):
    params = {'url': text, 'length': 3}
    response = requests.get(BASE_URL, headers=headers, params=params)
    if response.status_code == 200:
        summary = response.json().get('summary')
        return jsonify({'summary': summary})
    else:
        return jsonify({'error': 'Failed to fetch summary'}), response.status_code

# Route to handle input from POST request
@app.route('/', methods=['POST'])
def summarize_from_post():
    data = request.get_json()
    text = data.get('text')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    params = {'url': text, 'length': 3}
    response = requests.get(BASE_URL, headers=headers, params=params)
    if response.status_code == 200:
        summary = response.json().get('summary')
        return jsonify({'summary': summary})
    else:
        return jsonify({'error': 'Failed to fetch summary'}), response.status_code


if __name__ == '__main__':
    app.run(debug=True)