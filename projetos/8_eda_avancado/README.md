# Mini-projeto — 07_eda_avancado — EDA avançado e qualidade


Este mini-projeto consolida o módulo **07_eda_avancado** em um entregável de **portfólio**.
- Tempo estimado: 15–30 min
- Trilhas: eda, performance


## Entregável (portfólio)

- Notebook: [`01_entregavel_portfolio.ipynb`](./01_entregavel_portfolio.ipynb)
- Evidências:
  - `assets/` (imagens/HTML)
  - `reports/` (Markdown/JSON)
  - `outputs/` (parquet/modelos)


## Objetivo
Aplicar um checklist de qualidade, construir features (ex.: RFM) e gerar insights exportáveis.

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
- [`notebooks/07_eda_avancado/01_missing_outliers_validacoes.ipynb`](../../notebooks/07_eda_avancado/01_missing_outliers_validacoes.ipynb)
- [`notebooks/07_eda_avancado/02_distribuicoes_grupos_storytelling.ipynb`](../../notebooks/07_eda_avancado/02_distribuicoes_grupos_storytelling.ipynb)
- [`notebooks/07_eda_avancado/03_feature_engineering_rfm_parquet.ipynb`](../../notebooks/07_eda_avancado/03_feature_engineering_rfm_parquet.ipynb)
- [`notebooks/07_eda_avancado/04_narrativa_insights_exportaveis.ipynb`](../../notebooks/07_eda_avancado/04_narrativa_insights_exportaveis.ipynb)

### Scripts
- [`scripts/07_eda_avancado/01_missing_outliers_validacoes.py`](../../scripts/07_eda_avancado/01_missing_outliers_validacoes.py)
- [`scripts/07_eda_avancado/02_distribuicoes_grupos_storytelling.py`](../../scripts/07_eda_avancado/02_distribuicoes_grupos_storytelling.py)
- [`scripts/07_eda_avancado/03_feature_engineering_rfm_parquet.py`](../../scripts/07_eda_avancado/03_feature_engineering_rfm_parquet.py)
- [`scripts/07_eda_avancado/04_narrativa_insights_exportaveis.py`](../../scripts/07_eda_avancado/04_narrativa_insights_exportaveis.py)

## Perguntas de negócio (modelo)
Use 3–5 perguntas para guiar sua análise. Exemplos:
- Onde estão as maiores oportunidades (região, categoria, canal)?
- O que mudou ao longo do tempo (tendência/sazonalidade)?
- Quais segmentos concentram receita/margem?
- Existem anomalias (outliers) ou problemas de qualidade?

## Entregáveis (portfólio)
- Relatório de qualidade (missing/outliers/regras) e ações
- Features no nível de cliente (ex.: RFM) em Parquet
- Insights exportados (CSV/JSON) em `dados/output/`

## Checklist de entrega
- [ ] Notebook com narrativa (perguntas → análises → conclusão)
- [ ] Export de artefatos (quando fizer sentido): `dados/processed/` e/ou `dados/output/`
- [ ] Evidências em `assets/` (imagens ou prints)
- [ ] README atualizado com resultados e próximos passos

## Evidências (o que colocar no GitHub)
- 1 gráfico de distribuição com highlight do insight
- Arquivo de features (`.parquet`) e exemplo de consumo (DuckDB/Pandas)

## Próximos passos
- Criar regras por coluna e falhar o pipeline se violar
- Gerar um resumo automático (markdown) para stakeholder

## Créditos
Este projeto faz parte da mentoria **Python para Dados**.
## Como gerar evidências

1- Abra o notebook do entregável  
2- Execute as células até o fim  
3- Faça commit dos arquivos gerados em `assets/`, `reports/` e `outputs/`
