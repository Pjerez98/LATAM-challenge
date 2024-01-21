from typing import List, Tuple
from datetime import datetime
from collections import defaultdict
from load_tweets import load_tweets
from collections import Counter

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:

    try:
        # Intenta cargar los tweets desde el archivo
        tweets = load_tweets(file_path)
    except Exception as e:
        print(f"Error al cargar tweets: {e}")
        return []

    try:
        # Para cada tweet obtenemos su fecha y usuario respectivo
        tweets_fechas = [datetime.strptime(tweet["date"], "%Y-%m-%dT%H:%M:%S%z").date() for tweet in tweets]
        tweets_users = [tweet['user']['username'] for tweet in tweets]

    except (KeyError, ValueError) as e:
        print(f"Error al procesar tweets: {e}")
        return []

    try:
        # Usa Counter para los contadores
        contador_fechas = Counter(tweets_fechas)
        contador_users = Counter(tweets_users)

        # Obtén los 10 elementos más comunes de fechas y usuarios
        top_10_fechas = contador_fechas.most_common(10)
        top_10_users = contador_users.most_common(10)

        # Combina fechas y usuarios en una lista de tuplas
        top_dates_users = [(fecha, user) for (fecha, _), (user, _) in zip(top_10_fechas, top_10_users)]

        return top_dates_users
    
    except Exception as e:
        print(f"Error al procesar contadores: {e}")
        return []

