# Mini-projeto — 05_polars — Polars para performance


Este mini-projeto consolida o módulo **05_polars** em um entregável de **portfólio**.
- Tempo estimado: 15–30 min
- Trilhas: performance


## Entregável (portfólio)

- Notebook: [`01_entregavel_portfolio.ipynb`](./01_entregavel_portfolio.ipynb)
- Evidências:
  - `assets/` (imagens/HTML)
  - `reports/` (Markdown/JSON)
  - `outputs/` (parquet/modelos)


## Objetivo
Recriar um pipeline comum (limpeza + agregação) com Polars e comparar com Pandas.

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
- [`notebooks/05_polars/01_polars_expressions_lazy.ipynb`](../../notebooks/05_polars/01_polars_expressions_lazy.ipynb)

### Scripts
- [`scripts/05_polars/01_polars_expressions_lazy.py`](../../scripts/05_polars/01_polars_expressions_lazy.py)

## Perguntas de negócio (modelo)
Use 3–5 perguntas para guiar sua análise. Exemplos:
- Onde estão as maiores oportunidades (região, categoria, canal)?
- O que mudou ao longo do tempo (tendência/sazonalidade)?
- Quais segmentos concentram receita/margem?
- Existem anomalias (outliers) ou problemas de qualidade?

## Entregáveis (portfólio)
- Pipeline em Polars (lazy) com ao menos 2 agregações
- Comparação simples de tempo (Pandas vs Polars) e conclusão

## Checklist de entrega
- [ ] Notebook com narrativa (perguntas → análises → conclusão)
- [ ] Export de artefatos (quando fizer sentido): `dados/processed/` e/ou `dados/output/`
- [ ] Evidências em `assets/` (imagens ou prints)
- [ ] README atualizado com resultados e próximos passos

## Evidências (o que colocar no GitHub)
- Trecho de código com `LazyFrame` e explicação do ganho
- Tabela final com principais métricas

## Próximos passos
- Testar leitura de Parquet grande (quando usar dataset real)
- Comparar memória (aproximação) e tempo em 3 execuções

## Créditos
Este projeto faz parte da mentoria **Python para Dados**.
## Como gerar evidências

1- Abra o notebook do entregável  
2- Execute as células até o fim  
3- Faça commit dos arquivos gerados em `assets/`, `reports/` e `outputs/`
