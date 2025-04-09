from flask import Blueprint, request, jsonify

chatbot_blueprint = Blueprint('chatbot', __name__)

user_sessions = {}

@chatbot_blueprint.route('/message', methods=['POST'])
def handle_message():
    data = request.get_json()
    username = data.get('username')
    message = data.get('message')

#retrieve or initialize the session
    session = user_sessions.get(username, {"stage": "greeting"})

    if session["stage"] == "greetings":
        response = "Hi, I'm Pinki, what game vibe are you feeling today? (e.g., RPG, shooter, indie, chill)"
        session["stage"] = "game_query"
    elif session["stage"] == "game_query":
        #save game type preference
        session["game_preference"] = message
        response = "Purr! In this economy, what does your budget look like? (Give me a range like 0 - 20)"
        session["stage"] = "price"
    elif session["stage"] == "price":
        session["price_range"] = message
        response = "Noted! One more thing: will you be playing solo or with some friends?"
        session["stage"] = "multiplayer"
    elif session["stage"] == "multiplayer":
        session["multiplayer"] = message.lower()

        #CALL RECOMMENDATION FUNCTION
        response = "Ok gimme a second to see what I can find for you."
        #store final session data for recommendation processing
        user_sessions[username] = session
    
    else:
        response = "I'm not really sure what you're waffling about. Talk to me when you mean buisness."

    user_sessions[username] = session
    return jsonify({"reply": response})