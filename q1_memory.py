from typing import List, Tuple
from datetime import datetime
from load_tweets import load_tweets
from collections import Counter


def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    try:
        # Intenta cargar los tweets desde el archivo
        tweets = load_tweets(file_path)
    except Exception as e:
        print(f"Error al cargar tweets: {e}")
        return []

    # Usa Counter directamente para los contadores
    contador_fechas = Counter()
    contador_users = Counter()

    try:
        # Procesa cada tweet y actualiza los contadores
        for tweet in tweets:
            try:
                fecha = datetime.strptime(tweet["date"], "%Y-%m-%dT%H:%M:%S%z").date()
                user = tweet["user"]["username"]

                contador_fechas[fecha] += 1
                contador_users[user] += 1
            except (KeyError, ValueError) as e:
                print(f"Error al procesar tweet: {e}")
    except Exception as e:
        print(f"Error al procesar tweets: {e}")
        return []

    try:
        # Obtiene las top 10 fechas y usuarios
        top_10_fechas = contador_fechas.most_common(10)
        top_10_users = contador_users.most_common(10)

        # Combina fechas y usuarios en una lista de tuplas
        top_dates_users = [(fecha, user) for (fecha, _), (user, _) in zip(top_10_fechas, top_10_users)]

        return top_dates_users
    except Exception as e:
        print(f"Error al procesar contadores: {e}")
        return []