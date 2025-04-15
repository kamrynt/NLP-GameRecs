import pandas as pd
from sentence_transformers import SentenceTransformer, util
import torch

model = SentenceTransformer('all-MiniLM-L6-v2')

# Load datasets
games_df = pd.read_csv("data/games.csv")
features_df = pd.read_csv("data/games-features-edit.csv")
merged_df = pd.read_csv("data/merged_data.csv")

# Rename conflicting columns
games_df = games_df.rename(columns={"genre": "genre_main"})
merged_df = merged_df.rename(columns={"genre": "genre_alt"})

# Clean nulls
games_df.dropna(subset=["Summary"], inplace=True)
merged_df.dropna(subset=["Game Description"], inplace=True)

# Merge all datasets on Title
combined_df = games_df.merge(features_df, on="Title", how="left")
combined_df = combined_df.merge(merged_df, on="Title", how="left")
combined_df.fillna("", inplace=True)

# Embed summaries for SBERT matching
summaries = combined_df["Summary"].tolist()
summary_embeddings = model.encode(summaries, convert_to_tensor=True)

def recommend_games(user_input, top_n=3):
    user_embedding = model.encode(user_input, convert_to_tensor=True)
    cosine_scores = util.pytorch_cos_sim(user_embedding, summary_embeddings)[0]
    top_results = torch.topk(cosine_scores, k=top_n)

    results = []
    for score, idx in zip(top_results[0], top_results[1]):
        game = combined_df.iloc[int(idx)]
        results.append({
            "title": game["Title"],
            "summary": game["Summary"][:300] + "...",
            "price": game.get("price") or game.get("Discounted Price") or game.get("Price") or "N/A",
            "metacritic": game.get("Metacritic", "N/A") or "N/A",
            "store_url": game.get("store_url") if isinstance(game.get("store_url"), str) and game.get("store_url").startswith("http") else None,
            "genre": eval(game["genre_main"]) if isinstance(game["genre_main"], str) and game["genre_main"].startswith("[") else [],
            "review": str(game.get("Recent Reviews Summary") or "No reviews available"),
            "score": float(score)
        })
    return results
