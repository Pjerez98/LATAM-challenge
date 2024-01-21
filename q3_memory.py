from typing import List, Tuple
from load_tweets import load_tweets
from collections import Counter

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    try:
        tweets = load_tweets(file_path)
    except Exception as e:
        print(f"Error loading tweets from {file_path}: {e}")
        return []  # Devolver una lista vacía en caso de error

    mentions_counter = Counter()

    for tweet in tweets:
        try:
            mentions = tweet.get("mentionedUsers")
            if mentions:
                for mention in mentions:
                    username = mention.get("username")
                    if username:
                        mentions_counter[username] += 1
        except Exception as e:
            print(f"Error processing a tweet: {e}")

    top_users = mentions_counter.most_common(10)

    return top_users

