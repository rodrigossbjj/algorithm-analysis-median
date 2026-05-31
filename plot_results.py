"""
plot_results.py
Executa o benchmark e plota os tempos comparativos entre os dois algoritmos.
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# Importa o módulo principal
from benchmark.runner import benchmark

SIZES   = [1_000, 5_000, 10_000, 30_000, 50_000, 75_000, 100_000]
REPEATS = 5

# ── Roda o benchmark ──────────────────────────────────────────────
results = benchmark(SIZES, REPEATS)

sizes   = results["sizes"]
t1_ms   = [t * 1000 for t in results["algo1_times"]]   # ms
t2_ms   = [t * 1000 for t in results["algo2_times"]]   # ms

# ── Plot ──────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle("6.10 — Mediana de Dois Bancos de Dados\nComparação de Algoritmos",
             fontsize=14, fontweight="bold", y=1.02)

# Paleta
C1, C2 = "#E63946", "#457B9D"

# ── Gráfico 1: Escala linear ──────────────────────────────────────
ax = axes[0]
ax.plot(sizes, t1_ms, "o-", color=C1, linewidth=2, markersize=6,
        label="Algo 1 — Merge + Sort  O(n log n)")
ax.plot(sizes, t2_ms, "s--", color=C2, linewidth=2, markersize=6,
        label="Algo 2 — Divisão e Conquista  O(log n)")

ax.set_title("Tempo médio (escala linear)", fontsize=12)
ax.set_xlabel("Tamanho de cada vetor (n)", fontsize=11)
ax.set_ylabel("Tempo médio (ms)", fontsize=11)
ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
ax.legend(fontsize=9)
ax.grid(True, linestyle="--", alpha=0.5)

# ── Gráfico 2: Escala logarítmica ────────────────────────────────
ax = axes[1]
ax.plot(sizes, t1_ms, "o-", color=C1, linewidth=2, markersize=6,
        label="Algo 1 — Merge + Sort  O(n log n)")
ax.plot(sizes, t2_ms, "s--", color=C2, linewidth=2, markersize=6,
        label="Algo 2 — Divisão e Conquista  O(log n)")

ax.set_yscale("log")
ax.set_title("Tempo médio (escala log — eixo y)", fontsize=12)
ax.set_xlabel("Tamanho de cada vetor (n)", fontsize=11)
ax.set_ylabel("Tempo médio (ms) — log", fontsize=11)
ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter("%.4f"))
ax.legend(fontsize=9)
ax.grid(True, linestyle="--", alpha=0.5, which="both")

plt.tight_layout()
import os

os.makedirs("outputs", exist_ok=True)
out_path = os.path.join("outputs", "median_benchmark.png")
plt.savefig(out_path, dpi=150, bbox_inches="tight")
print(f"Gráfico salvo em {out_path}")
plt.show()
