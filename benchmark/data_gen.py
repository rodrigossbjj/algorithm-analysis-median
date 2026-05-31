import random
from typing import List, Tuple


def generate_sorted_pair(size: int, value_range: int = 10_000_000) -> Tuple[List[int], List[int]]:
    """Gera dois vetores ordenados de inteiros aleatórios com o mesmo tamanho."""
    a = sorted(random.randint(0, value_range) for _ in range(size))
    b = sorted(random.randint(0, value_range) for _ in range(size))
    return a, b
