from flask import Blueprint, request, jsonify
import pandas as pd

recommendation_blueprint = Blueprint('recommendations', __name__)

games_data = pd.read_csv('data/games.csv')
steam_data = pd.read_csv('data/games-features-edit')
price_data = pd.read_csv('data/merged_data.csv')

all_games = pd.merge(games_data, steam_data, price_data, on='Title', how="inner")

@recommendation_blueprint.route('/get', methods=['POST'])
def get_recommendations():
    data = request.get_json()
    
    game_preference = data.get('game_preference')
    price_range = data.get('price_range')
    multiplayer_pref = data.get('multiplayer')

    try:
        low, high = map(float, price_range.split('-'))
    except Exception as e:
        return jsonify({"msg": "Invalid price range format. Use something like 0-20."}), 400

    filtered_games = all_games[
        all_games['genre'].str.contains(game_preference, case=False, na=False) &
        (all_games['price'] >= low) &
        (all_games['price'] <= high)
    ]
    if "squad" in multiplayer_pref or "friends" in multiplayer_pref:
        filtered_games = filtered_games[filtered_games['multiplayer'] == True]

    filtered_games = filtered_games.sort_values(by="rating", ascending=False)

    recs = []
    for _, row in filtered_games.head(5).iterrows():
        recs.append({
            "game_title": row.get("Title"),
            "rating": row.get("rating"),
            "price": row.get("price"),
            "link": row.get("store_url")
        })

    return jsonify({"recommendations": recs})

