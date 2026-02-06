# Mini-projeto — 02_numpy — NumPy para simulação e estatística


Este mini-projeto consolida o módulo **02_numpy** em um entregável de **portfólio**.
- Tempo estimado: 15–30 min
- Trilhas: core


## Entregável (portfólio)

- Notebook: [`01_entregavel_portfolio.ipynb`](./01_entregavel_portfolio.ipynb)
- Evidências:
  - `assets/` (imagens/HTML)
  - `reports/` (Markdown/JSON)
  - `outputs/` (parquet/modelos)


## Objetivo
Simular cenários de receita usando amostragem/bootstrapping e resumir resultados com percentis e intervalos.

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
- [`notebooks/02_numpy/01_arrays_broadcast_boolean.ipynb`](../../notebooks/02_numpy/01_arrays_broadcast_boolean.ipynb)
- [`notebooks/02_numpy/02_estatistica_random_simulacao.ipynb`](../../notebooks/02_numpy/02_estatistica_random_simulacao.ipynb)

### Scripts
- [`scripts/02_numpy/01_arrays_broadcast_boolean.py`](../../scripts/02_numpy/01_arrays_broadcast_boolean.py)
- [`scripts/02_numpy/02_estatistica_random_simulacao.py`](../../scripts/02_numpy/02_estatistica_random_simulacao.py)


## Entregáveis (portfólio)
- Relatório simples com percentis (p50/p75/p90/p95) e uma recomendação
- Gráfico opcional de distribuição (histograma) em `assets/`

## Checklist de entrega
- [ ] Notebook com narrativa (perguntas → análises → conclusão)
- [ ] Export de artefatos (quando fizer sentido): `dados/processed/` e/ou `dados/output/`
- [ ] Evidências em `assets/` (imagens ou prints)
- [ ] README atualizado com resultados e próximos passos

## Evidências (o que colocar no GitHub)
- Explicação curta do porquê usar percentis em vez de média
- Código vetorizado (sem loops desnecessários)

## Próximos passos
- Comparar performance: loop vs vetorizado
- Simular cenários com variação de preço/desconto

## Créditos
Este projeto faz parte da mentoria **Python para Dados**.
## Como gerar evidências

1- Abra o notebook do entregável  
2- Execute as células até o fim  
3- Faça commit dos arquivos gerados em `assets/`, `reports/` e `outputs/`
