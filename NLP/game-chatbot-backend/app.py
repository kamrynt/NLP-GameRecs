from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot.recommender import recommend_games

app = Flask(__name__)
CORS(app)  # Allow requests from frontend

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "")
    if not message:
        return jsonify({"reply": "Please enter a valid message."}), 400
    
    recommendations = recommend_games(message)
    reply = "Here are some games you might like:\n" + "\n".join(
        [f"🎮 {game['Title']}: {game['Summary'][:120]}..." for game in recommendations]
    )
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
