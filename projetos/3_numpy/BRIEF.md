# BRIEF — 02_numpy

## Objetivo
Aplicar Numpy em um problema de simulação/estatística e documentar o raciocínio.

## Dataset
Use `dados/sample/sales.csv` (coluna `revenue`).

## Problema
Você quer prever uma faixa provável de receita total para o próximo mês, assumindo que o padrão de pedidos é parecido com o histórico.

## Entregáveis
1- `notebook.ipynb` com:
   - distribuição de revenue (percentis)
   - simulação (>= 1.000 simulações)
   - interpretação: p05/p50/p95
2- `README.md` com a leitura do resultado (em linguagem de negócio)

## Regras
- Use `np.random.default_rng`
- Evite loops quando possível (prefira operações vetorizadas)

## Extra (opcional)
- Simular com desconto de 5% e comparar cenários
