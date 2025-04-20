from flask import Flask, request, jsonify
from flask_cors import CORS
from nlp_engine import extract_info

app = Flask(__name__)
CORS(app)

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    note = data.get('note', '')
    patient = data.get('patient', 'Non spécifié')
    cycle = data.get('cycle', 'Non spécifié')

    result = extract_info(note)
    result['patient'] = patient
    result['cycle'] = cycle

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)