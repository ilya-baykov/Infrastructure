def construct_profitability_matrix(vector: list[float]) -> dict:
    return {day: vector[day] / vector[day - 1] for day in range(1, len(vector))}

