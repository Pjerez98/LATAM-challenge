from typing import List, Tuple
from datetime import datetime
from load_tweets import load_tweets
from collections import Counter

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    tweets = load_tweets(file_path)
    mentions = [tweet["mentionedUsers"] for tweet in tweets]
    usernames = [username['username'] for mention in mentions if mention is not None for username in mention if username is not None]

    # Conteo de menciones
    mentions_counter = Counter(usernames)

    # Encontrar los top 10 usuarios mencionados
    top_users = mentions_counter.most_common(10)

    return top_users