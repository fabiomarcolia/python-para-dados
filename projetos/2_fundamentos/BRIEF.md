# BRIEF — 01_fundamentos

## Objetivo
Fazer uma análise simples **sem depender do Pandas**, usando Python “puro” (listas, dicts, funções).
Isso ajuda muito quem vem de Excel/Power BI a entender a base do processamento.

## Dataset
Use `dados/sample/sales.csv` (ou substitua por um dataset do repo `bases-dados-analytics-powerbi-ml`).

## Entregáveis
1- `notebook.ipynb`
2- `README.md` (contexto, passos, conclusões)
3- `dados/output/summary.json` com um resumo do dataset

## Regras
- Não usar `pandas` nesta etapa (é proposital).
- Código comentado e funções pequenas.

## Perguntas que você deve responder
1- Qual a receita total?
2- Quais as 3 regiões com maior receita?
3- Qual categoria tem maior ticket médio?
4- Existe algum outlier evidente em revenue?

## Extra (opcional)
- Criar uma função `validate_schema(rows, required_cols)`
