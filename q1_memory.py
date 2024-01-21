from typing import List, Tuple
from datetime import datetime
from load_tweets import load_tweets
from collections import Counter

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    tweets = load_tweets(file_path)

    # Contadores para fechas y usuarios
    contador_fechas = Counter()
    contador_users = Counter()

    # Procesar cada tweet una vez y actualizar los contadores
    for tweet in tweets:
        fecha = datetime.strptime(tweet["date"], "%Y-%m-%dT%H:%M:%S%z").date()
        user = tweet["user"]["username"]

        contador_fechas[fecha] += 1
        contador_users[user] += 1

    # Obtener las top 10 fechas y usuarios
    top_10_fechas = contador_fechas.most_common(10)
    top_10_users = contador_users.most_common(10)

    # Combinar fechas y usuarios en una lista de tuplas
    top_dates_users = [(fecha[0], user[0]) for fecha, user in zip(top_10_fechas, top_10_users)]

    return top_dates_users