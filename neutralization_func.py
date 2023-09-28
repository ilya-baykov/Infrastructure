A = [1, 5, 3, 4, 5, 1, 4, 56, 75, 5, 3, 2, 12, 4]


def neutralization(vector: list[int]) -> list[float]:
    return [int(i) - (sum(vector) / len(vector)) for i in vector]


print(neutralization(A))
