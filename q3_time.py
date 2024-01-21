from typing import List, Tuple
from load_tweets import load_tweets
from collections import Counter

def q3_time(file_path: str) -> List[Tuple[str, int]]:

    try:
        # Intenta cargar los tweets desde el archivo
        tweets = load_tweets(file_path)
    except Exception as e:
        print(f"Error al cargar tweets: {e}")
        return []
   
    
    try :
        mentions = [tweet["mentionedUsers"] for tweet in tweets]
        usernames = [username['username'] for mention in mentions if mention is not None for username in mention if username is not None]
        mentions_counter = Counter(usernames)
        top_users = mentions_counter.most_common(10)

    except Exception as e:
        print(f'Error al procesar usuarios y menciones: {e}')
        return []
    
    return top_users

