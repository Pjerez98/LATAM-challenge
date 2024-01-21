from typing import List, Tuple

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    tweets = load_tweets(file_path)
    contenidos = [tweet['content'] for tweet in tweets]

    # Se obtiene los emojis ÚNICOS presentes en cada tweet, para ver cual es el más común en todos los tweets,
    emojis = [list(set([fila['emoji'] for fila in emoji.emoji_list(contenido)])) for contenido in contenidos]
    emojis_plano = [emojii for lista_emojis in emojis for emojii in lista_emojis]
    emojis_plano
    
    # Conteo de emojis
    emojis_counter = Counter(emojis_plano)
    
    # Encontrar los top 10 emojis
    top_emojis = emojis_counter.most_common(10)

    return top_emojis