# Mini-projeto — 08_machine_learning — Machine Learning baseline


Este mini-projeto consolida o módulo **08_machine_learning** em um entregável de **portfólio**.
- Tempo estimado: 15–30 min
- Trilhas: ml


## Entregável (portfólio)

- Notebook: [`01_entregavel_portfolio.ipynb`](./01_entregavel_portfolio.ipynb)
- Evidências:
  - `assets/` (imagens/HTML)
  - `reports/` (Markdown/JSON)
  - `outputs/` (parquet/modelos)


## Objetivo
Criar um baseline de classificação com pipeline do scikit-learn, métricas e interpretação básica.

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
- [`notebooks/08_machine_learning/01_baseline_classificacao.ipynb`](../../notebooks/08_machine_learning/01_baseline_classificacao.ipynb)
- [`notebooks/08_machine_learning/02_split_metricas_baseline.ipynb`](../../notebooks/08_machine_learning/02_split_metricas_baseline.ipynb)
- [`notebooks/08_machine_learning/03_pipeline_comparacao_modelos.ipynb`](../../notebooks/08_machine_learning/03_pipeline_comparacao_modelos.ipynb)
- [`notebooks/08_machine_learning/04_tuning_interpretabilidade.ipynb`](../../notebooks/08_machine_learning/04_tuning_interpretabilidade.ipynb)

### Scripts
- [`scripts/08_machine_learning/01_baseline_classificacao.py`](../../scripts/08_machine_learning/01_baseline_classificacao.py)
- [`scripts/08_machine_learning/02_split_metricas_baseline.py`](../../scripts/08_machine_learning/02_split_metricas_baseline.py)
- [`scripts/08_machine_learning/03_pipeline_comparacao_modelos.py`](../../scripts/08_machine_learning/03_pipeline_comparacao_modelos.py)
- [`scripts/08_machine_learning/04_tuning_interpretabilidade.py`](../../scripts/08_machine_learning/04_tuning_interpretabilidade.py)

## Perguntas de negócio (modelo)
Use 3–5 perguntas para guiar sua análise. Exemplos:
- Onde estão as maiores oportunidades (região, categoria, canal)?
- O que mudou ao longo do tempo (tendência/sazonalidade)?
- Quais segmentos concentram receita/margem?
- Existem anomalias (outliers) ou problemas de qualidade?

## Entregáveis (portfólio)
- Baseline com métricas (precision/recall/f1/roc_auc) em `dados/output/ml/`
- Pipeline com pré-processamento + modelo + avaliação
- Interpretação simples (feature importance) e próximos passos

## Checklist de entrega
- [ ] Notebook com narrativa (perguntas → análises → conclusão)
- [ ] Export de artefatos (quando fizer sentido): `dados/processed/` e/ou `dados/output/`
- [ ] Evidências em `assets/` (imagens ou prints)
- [ ] README atualizado com resultados e próximos passos

## Evidências (o que colocar no GitHub)
- Tabela de comparação de modelos e escolha do baseline
- Gráfico/print de feature importance

## Próximos passos
- Adicionar validação cruzada e busca de hiperparâmetros
- Criar um relatório final (markdown) com conclusões

## Créditos
Este projeto faz parte da mentoria **Python para Dados**.
## Como gerar evidências

1- Abra o notebook do entregável  
2- Execute as células até o fim  
3- Faça commit dos arquivos gerados em `assets/`, `reports/` e `outputs/`
