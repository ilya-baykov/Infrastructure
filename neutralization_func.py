def neutralization(vector: list[float]) -> list[float]:
    """"
        Возвращает нейтрализованный вектор по формуле neutralization_v = v  -  avg(v), где
        avg(v) - среднее значение v.
    """
    return [int(i) - (sum(vector) / len(vector)) for i in vector]
