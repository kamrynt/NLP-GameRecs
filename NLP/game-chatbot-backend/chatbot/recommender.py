import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
df = pd.read_csv("data/games.csv")
df.dropna(subset=["Summary"], inplace=True)

# Fit TF-IDF vectorizer on game summaries
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(df["Summary"])

def recommend_games(user_input, top_n=3):
    # Transform the input to vector
    input_vec = vectorizer.transform([user_input])
    # Compute cosine similarity
    cosine_similarities = cosine_similarity(input_vec, tfidf_matrix).flatten()
    # Get top N indices
    top_indices = cosine_similarities.argsort()[-top_n:][::-1]
    # Return top games
    return df.iloc[top_indices][["Title", "Summary"]].to_dict(orient="records")
