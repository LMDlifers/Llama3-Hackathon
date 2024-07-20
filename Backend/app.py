from flask import Flask, request, jsonify
from fetch_data import fetch_social_media_data
from preprocess_data import preprocess_data
from generate_embeddings import generate_embeddings
from analyze_mental_health import analyze_mental_health

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json.get('data')
    preprocessed_data = preprocess_data(data)
    index = generate_embeddings(preprocessed_data)
    analysis_results = analyze_mental_health(index, "signs of mental health issues")
    return jsonify(analysis_results)

if __name__ == '__main__':
    app.run(debug=True)
