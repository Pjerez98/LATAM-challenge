from typing import List, Tuple
import json  

def load_tweets(file_path: str) -> List[dict]:
    tweets = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            tweet_data = json.loads(line)
            tweets.append(tweet_data)
    return tweets