A = [1, 5, 3, 4, 5, 1, 4, 56, 75, 5, 3, 2, 12, 4]


def normalize(vector: list[int]) -> list[int]:
    """"
        Возвращает нормализованный вектор по формуле normalized_v = v / ||v||, где
        ||v|| = ||v|| = sqrt(v₁² + v₂² + ... + vₙ²).
    """
    return [int(i) / (sum([int(i) ** 2 for i in vector])) ** 0.5 for i in vector]
