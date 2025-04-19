from flask import Flask, request, jsonify
from flask_cors import CORS
from nlp_engine import extract_info

app = Flask(__name__)
CORS(app)

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    note = data.get('note', '')
    response = extract_info(note)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
