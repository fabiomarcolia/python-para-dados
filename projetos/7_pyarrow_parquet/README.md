# Mini-projeto — 06_pyarrow_parquet — PyArrow e Parquet


Este mini-projeto consolida o módulo **06_pyarrow_parquet** em um entregável de **portfólio**.
- Tempo estimado: 15–30 min
- Trilhas: performance


## Entregável (portfólio)

- Notebook: [`01_entregavel_portfolio.ipynb`](./01_entregavel_portfolio.ipynb)
- Evidências:
  - `assets/` (imagens/HTML)
  - `reports/` (Markdown/JSON)
  - `outputs/` (parquet/modelos)


## Objetivo
Construir um pipeline com Parquet (particionado) e consultas rápidas com DuckDB.

## Dataset
- Padrão (rápido): `dados/sample/` (já vem no repositório)
- Real (portfólio): adicionar o repo `bases-dados-analytics-powerbi-ml` em `dados/source/` (submodule ou clone)

## Como rodar
Na raiz do repositório:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate
pip install -r requirements.txt
```

Depois, siga o notebook recomendado (ou rode os scripts):

### Notebooks
- [`notebooks/06_pyarrow_parquet/01_pyarrow_parquet_particionamento.ipynb`](../../notebooks/06_pyarrow_parquet/01_pyarrow_parquet_particionamento.ipynb)

### Scripts
- [`scripts/06_pyarrow_parquet/01_pyarrow_parquet_particionamento.py`](../../scripts/06_pyarrow_parquet/01_pyarrow_parquet_particionamento.py)

## Perguntas de negócio (modelo)
Use 3–5 perguntas para guiar sua análise. Exemplos:
- Onde estão as maiores oportunidades (região, categoria, canal)?
- O que mudou ao longo do tempo (tendência/sazonalidade)?
- Quais segmentos concentram receita/margem?
- Existem anomalias (outliers) ou problemas de qualidade?

## Entregáveis (portfólio)
- Dataset particionado em `dados/processed/` (Parquet)
- Exemplos de leitura seletiva (colunas e filtros) com DuckDB
- README com benchmarks simples (tempo e tamanho em disco)

## Checklist de entrega
- [ ] Notebook com narrativa (perguntas → análises → conclusão)
- [ ] Export de artefatos (quando fizer sentido): `dados/processed/` e/ou `dados/output/`
- [ ] Evidências em `assets/` (imagens ou prints)
- [ ] README atualizado com resultados e próximos passos

## Evidências (o que colocar no GitHub)
- Print do `duckdb` consultando o Parquet particionado
- Comparação: CSV vs Parquet (tamanho e tempo)

## Próximos passos
- Adicionar esquema (schema) explícito e validação
- Criar particionamento por dados/UF/categoria (conforme dataset)

## Créditos
Este projeto faz parte da mentoria **Python para Dados**.
## Como gerar evidências

1- Abra o notebook do entregável  
2- Execute as células até o fim  
3- Faça commit dos arquivos gerados em `assets/`, `reports/` e `outputs/`
