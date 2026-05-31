# Mediana de Dois Bancos de Dados

Implementação e benchmark de duas abordagens para calcular a mediana combinada
de duas listas ordenadas.

Descrição rápida
- Problema: dados dois vetores ordenados, calcular a mediana da união dos elementos.
- Algoritmos comparados:
  - `median_merge_sort` — juntar e ordenar (complexidade O(n log n)).
  - `median_divide_and_conquer` — divisão e conquista / busca binária (complexidade O(log min(m,n))).

Estrutura do projeto
```
projeto/
├── algorithms/        # Implementações dos algoritmos
├── benchmark/         # Runner e gerador de dados
├── tests/             # Casos de teste (pytest)
├── plot_results.py    # Gera e salva o gráfico comparativo
├── main.py            # Entrada simples para executar o plot/benchmark
├── requirements.txt
└── README.md
```

Como usar
1. Instale dependências:
```bash
python -m pip install -r requirements.txt
```
2. Executar o benchmark e gerar o gráfico:
```bash
python main.py
```
O gráfico é salvo em `outputs/median_benchmark.png`.

Testes
```bash
python -m pytest -q
```

Notas
- Os tamanhos testados pelo benchmark estão configurados entre 10^3 e 10^5 em `benchmark/runner.py`.
- `plot_results.py` chama o runner para obter os tempos médios e plota em escala linear e log.