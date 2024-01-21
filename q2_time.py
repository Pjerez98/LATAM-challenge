from typing import List, Tuple
from collections import Counter
from load_tweets import load_tweets
import emoji


def q2_time(file_path: str) -> List[Tuple[str, int]]:
    try:
        # Intenta cargar los tweets desde el archivo
        tweets = load_tweets(file_path)
    except Exception as e:
        print(f"Error al cargar tweets: {e}")
        return []

    emojis_counter = Counter()

    try:
        for tweet in tweets:
            try:
                contenidos = tweet['content']
                emojis = list(set([fila['emoji'] for fila in emoji.emoji_list(contenidos) if 'emoji' in fila]))
                emojis_counter.update(emojis)
            except KeyError:
                print("Error: 'content' no encontrado en el tweet.")
    except Exception as e:
        print(f"Error al procesar tweets: {e}")
        return []

    try:
        # Obtiene las top 10 emojis
        top_emojis = emojis_counter.most_common(10)
        return top_emojis
    except Exception as e:
        print(f"Error al procesar contadores: {e}")
        return []
