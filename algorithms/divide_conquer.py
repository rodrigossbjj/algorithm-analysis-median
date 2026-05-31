import math
from typing import List


def median_divide_and_conquer(a: List[int], b: List[int]) -> float:
    """Encontra a mediana da união de dois vetores ordenados em O(log(min(m,n)))."""
    if not a and not b:
        raise ValueError("Ambos os vetores estão vazios")

    # Garantir que 'a' seja o menor vetor
    if len(a) > len(b):
        a, b = b, a

    m, n = len(a), len(b)
    lo, hi = 0, m

    while lo <= hi:
        pa = (lo + hi) // 2
        pb = (m + n + 1) // 2 - pa

        max_left_a = a[pa - 1] if pa > 0 else -math.inf
        min_right_a = a[pa] if pa < m else math.inf
        max_left_b = b[pb - 1] if pb > 0 else -math.inf
        min_right_b = b[pb] if pb < n else math.inf

        if max_left_a <= min_right_b and max_left_b <= min_right_a:
            if (m + n) % 2 == 1:
                return float(max(max_left_a, max_left_b))
            return (max(max_left_a, max_left_b) + min(min_right_a, min_right_b)) / 2.0
        elif max_left_a > min_right_b:
            hi = pa - 1
        else:
            lo = pa + 1

    raise ValueError("Entrada inválida: certifique-se que os vetores estejam ordenados")
