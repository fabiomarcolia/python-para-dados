# Mini-projeto — 04_visualizacao — Visualização e storytelling


Este mini-projeto consolida o módulo **04_visualizacao** em um entregável de **portfólio**.
- Tempo estimado: 15–30 min
- Trilhas: eda


## Entregável (portfólio)

- Notebook: [`01_entregavel_portfolio.ipynb`](./01_entregavel_portfolio.ipynb)
- Evidências:
  - `assets/` (imagens/HTML)
  - `reports/` (Markdown/JSON)
  - `outputs/` (parquet/modelos)


## Objetivo
Contar a história do dataset com gráficos claros e exportáveis para portfólio.

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
- [`notebooks/04_visualizacao/01_matplotlib_basico.ipynb`](../../notebooks/04_visualizacao/01_matplotlib_basico.ipynb)
- [`notebooks/04_visualizacao/02_seaborn_eda.ipynb`](../../notebooks/04_visualizacao/02_seaborn_eda.ipynb)
- [`notebooks/04_visualizacao/03_plotly_interativo.ipynb`](../../notebooks/04_visualizacao/03_plotly_interativo.ipynb)

### Scripts
- [`scripts/04_visualizacao/01_matplotlib_basico.py`](../../scripts/04_visualizacao/01_matplotlib_basico.py)
- [`scripts/04_visualizacao/02_seaborn_eda.py`](../../scripts/04_visualizacao/02_seaborn_eda.py)
- [`scripts/04_visualizacao/03_plotly_interativo.py`](../../scripts/04_visualizacao/03_plotly_interativo.py)

## Perguntas de negócio (modelo)
Use 3–5 perguntas para guiar sua análise. Exemplos:
- Onde estão as maiores oportunidades (região, categoria, canal)?
- O que mudou ao longo do tempo (tendência/sazonalidade)?
- Quais segmentos concentram receita/margem?
- Existem anomalias (outliers) ou problemas de qualidade?

## Entregáveis (portfólio)
- 3 gráficos (mínimo) exportados em `assets/`
- 1 gráfico com anotação (insight destacado)
- README com narrativa (contexto → análise → conclusão)

## Checklist de entrega
- [ ] Notebook com narrativa (perguntas → análises → conclusão)
- [ ] Export de artefatos (quando fizer sentido): `dados/processed/` e/ou `dados/output/`
- [ ] Evidências em `assets/` (imagens ou prints)
- [ ] README atualizado com resultados e próximos passos

## Evidências (o que colocar no GitHub)
- Antes/depois: gráfico ruim vs gráfico bom (opcional)
- Justificativa de escolha de gráfico (por que linha/coluna/boxplot)

## Próximos passos
- Criar um mini-dashboard em Plotly (1 página)
- Gerar gráficos automaticamente a partir de uma configuração (YAML/JSON)

## Créditos
Este projeto faz parte da mentoria **Python para Dados**.
## Como gerar evidências

1- Abra o notebook do entregável  
2- Execute as células até o fim  
3- Faça commit dos arquivos gerados em `assets/`, `reports/` e `outputs/`
