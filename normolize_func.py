def normalize(vector: list[float]) -> list[float]:
    """"
        Возвращает нормализованный вектор по формуле x / sum(|x1| + |x2| + ... + |xn|)
    """
    return [int(i) / sum([abs(int(elem)) for elem in vector]) for i in vector]
