def normalize(vector: list[float]) -> list[float]:
    """"
        Возвращает нормализованный вектор по формуле normalized_v = v / ||v||, где
        ||v|| = ||v|| = sqrt(v₁² + v₂² + ... + vₙ²).
    """
    return [int(i) / (sum([int(i) ** 2 for i in vector])) ** 0.5 for i in vector]


print(normalize([1, 2, 3]))
