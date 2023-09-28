from neutralization_func import neutralization
from normolize_func import normalize


def build_alpha(vector: list) -> list:
    return normalize(neutralization([-1 * vector[i - 1] / vector[i - 6] for i in range(6, len(list))]))
