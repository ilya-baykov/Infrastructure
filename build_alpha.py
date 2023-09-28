from neutralization_func import neutralization
from normolize_func import normalize


def build_alpha(vector: list) -> list:
    """"
        Заполняю массив в генераторе по формуле -close(i) ( d - 1) / close(i) ( d - 6 )
        Для полученного массива применяю поочерёдно нейтрализацию и нормализацию
    """
    return normalize(neutralization([-1 * vector[i - 1] / vector[i - 6] for i in range(6, len(list))]))
