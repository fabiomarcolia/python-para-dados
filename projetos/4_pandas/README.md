# Mini-projeto — 03_pandas — Pandas para EDA


Este mini-projeto consolida o módulo **03_pandas** em um entregável de **portfólio**.
- Tempo estimado: 15–30 min
- Trilhas: eda


## Entregável (portfólio)

- Notebook: [`01_entregavel_portfolio.ipynb`](./01_entregavel_portfolio.ipynb)
- Evidências:
  - `assets/` (imagens/HTML)
  - `reports/` (Markdown/JSON)
  - `outputs/` (parquet/modelos)


## Objetivo
Construir uma EDA organizada: limpeza, tipagem, agregações, joins e respostas para perguntas de negócio.

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
- [`notebooks/03_pandas/01_pandas_intro_limpeza.ipynb`](../../notebooks/03_pandas/01_pandas_intro_limpeza.ipynb)
- [`notebooks/03_pandas/02_groupby_pivot_agg.ipynb`](../../notebooks/03_pandas/02_groupby_pivot_agg.ipynb)
- [`notebooks/03_pandas/03_merge_join_concat.ipynb`](../../notebooks/03_pandas/03_merge_join_concat.ipynb)

### Scripts
- [`scripts/03_pandas/01_pandas_intro_limpeza.py`](../../scripts/03_pandas/01_pandas_intro_limpeza.py)
- [`scripts/03_pandas/02_groupby_pivot_agg.py`](../../scripts/03_pandas/02_groupby_pivot_agg.py)
- [`scripts/03_pandas/03_merge_join_concat.py`](../../scripts/03_pandas/03_merge_join_concat.py)

## Perguntas de negócio (modelo)
Use 3–5 perguntas para guiar sua análise. Exemplos:
- Onde estão as maiores oportunidades (região, categoria, canal)?
- O que mudou ao longo do tempo (tendência/sazonalidade)?
- Quais segmentos concentram receita/margem?
- Existem anomalias (outliers) ou problemas de qualidade?

## Entregáveis (portfólio)
- Notebook com 3–5 perguntas + análises
- Export de dataset limpo em `dados/processed/` (CSV/Parquet)
- README com 5 insights e próximos passos

## Checklist de entrega
- [ ] Notebook com narrativa (perguntas → análises → conclusão)
- [ ] Export de artefatos (quando fizer sentido): `dados/processed/` e/ou `dados/output/`
- [ ] Evidências em `assets/` (imagens ou prints)
- [ ] README atualizado com resultados e próximos passos

## Evidências (o que colocar no GitHub)
- Tabela final (top categorias/regiões) e explicação do insight
- Exemplo de join bem explicado (chaves, cardinalidade, riscos)

## Próximos passos
- Criar um dicionário de dados (colunas e regras)
- Adicionar uma validação de schema antes de salvar o dataset limpo

## Créditos
Este projeto faz parte da mentoria **Python para Dados**.
## Como gerar evidências

1- Abra o notebook do entregável  
2- Execute as células até o fim  
3- Faça commit dos arquivos gerados em `assets/`, `reports/` e `outputs/`
