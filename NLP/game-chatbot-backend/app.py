from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot.recommender import recommend_games

app = Flask(__name__)
CORS(app)  # Allow requests from frontend

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "")
    recommendations = recommend_games(message)
    return jsonify(recommendations)

if __name__ == "__main__":
    app.run(debug=True)
