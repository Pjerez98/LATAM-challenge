from typing import List, Tuple
from collections import Counter
from load_tweets import load_tweets
import emoji

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    tweets = load_tweets(file_path)
    emojis_counter = Counter()

    for tweet in tweets:
        contenidos = tweet['content']
        emojis = list(set([fila['emoji'] for fila in emoji.emoji_list(contenidos)]))
        emojis_counter.update(emojis)

    top_emojis = emojis_counter.most_common(10)

    return top_emojis