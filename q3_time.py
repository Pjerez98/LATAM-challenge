from typing import List, Tuple
from load_tweets import load_tweets
from collections import Counter

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    tweets = load_tweets(file_path)
    mentions_counter = Counter()

    for tweet in tweets:
        mentions = tweet.get("mentionedUsers")
        if mentions:
            usernames = [mention["username"] for mention in mentions if mention]
            mentions_counter.update(usernames)

    top_users = mentions_counter.most_common(10)

    return top_users