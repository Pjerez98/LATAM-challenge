from typing import List, Tuple
from datetime import datetime

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    tweets = load_tweets(file_path)
    # Por cada tweet, guardamos su fecha respectiva
    tweets_fechas = [datetime.strptime(tweet["date"], "%Y-%m-%dT%H:%M:%S%z").date() for tweet in tweets]
    # Luego, se cuenta el número de tweets por fecha, análogo a realizar un groupby por fecha y utilizar la función agregada count
    contador_fechas_tweets = Counter(tweets_fechas)
    # Finalmente, ordenamos de mayor a menor, y luego seleccionamos las top 10 fechas
    fechas_ordenadas_tweets = sorted(contador_fechas_tweets.items(), key=lambda x: x[1], reverse=True)
    top_10_fechas = fechas_ordenadas_tweets[:10]
    top_10_fechas

    # De la misma forma, procedemos con los usuarios

    # Por cada tweet, guardamos su usuario respectivo
    tweets_users = [tweet["user"]["username"] for tweet in tweets]
    # Luego, se cuenta el número de tweets por fecha, análogo a realizar un groupby por fecha y utilizar la función agregada count
    contador_fechas_users = Counter(tweets_users)
    # Finalmente, ordenamos de mayor a menor, y luego seleccionamos las top 10 fechas
    user_ordenados_tweets = sorted(contador_fechas_users.items(), key=lambda x: x[1], reverse=True)
    top_10_users = user_ordenados_tweets[:10]
    top_10_users

    top_dates_users = [(fecha[0],user[0]) for fecha,user in zip(top_10_fechas,top_10_users)]
    top_dates_users

    return top_dates_users
