# Mini-projeto — 01_fundamentos — Fundamentos aplicados a dados


Este mini-projeto consolida o módulo **01_fundamentos** em um entregável de **portfólio**.
- Tempo estimado: 15–30 min
- Trilhas: core, eda


## Entregável (portfólio)

- Notebook: [`01_entregavel_portfolio.ipynb`](./01_entregavel_portfolio.ipynb)
- Evidências:
  - `assets/` (imagens/HTML)
  - `reports/` (Markdown/JSON)
  - `outputs/` (parquet/modelos)


## Objetivo
Gerar um resumo confiável de um dataset usando Python puro (funções, dicts, listas) e salvar um relatório em JSON.

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
- [`notebooks/01_fundamentos/01_funcoes_comprehensions_para_dados.ipynb`](../../notebooks/01_fundamentos/01_funcoes_comprehensions_para_dados.ipynb)
- [`notebooks/01_fundamentos/02_pathlib_io_csv_json_parquet.ipynb`](../../notebooks/01_fundamentos/02_pathlib_io_csv_json_parquet.ipynb)
- [`notebooks/01_fundamentos/03_excecoes_logging_validacao.ipynb`](../../notebooks/01_fundamentos/03_excecoes_logging_validacao.ipynb)

### Scripts
- [`scripts/01_fundamentos/01_funcoes_comprehensions_para_dados.py`](../../scripts/01_fundamentos/01_funcoes_comprehensions_para_dados.py)
- [`scripts/01_fundamentos/02_pathlib_io_csv_json_parquet.py`](../../scripts/01_fundamentos/02_pathlib_io_csv_json_parquet.py)
- [`scripts/01_fundamentos/03_excecoes_logging_validacao.py`](../../scripts/01_fundamentos/03_excecoes_logging_validacao.py)

## Perguntas de negócio (modelo)
Use 3–5 perguntas para guiar sua análise. Exemplos:
- Onde estão as maiores oportunidades (região, categoria, canal)?
- O que mudou ao longo do tempo (tendência/sazonalidade)?
- Quais segmentos concentram receita/margem?
- Existem anomalias (outliers) ou problemas de qualidade?

## Entregáveis (portfólio)
- Arquivo `dados/output/summary.json` com estatísticas básicas e checagens
- Validações simples (tipos, nulos, duplicados) + tratamento de erros
- README do projeto com o que foi validado e o que foi encontrado

## Checklist de entrega
- [ ] Notebook com narrativa (perguntas → análises → conclusão)
- [ ] Export de artefatos (quando fizer sentido): `dados/processed/` e/ou `dados/output/`
- [ ] Evidências em `assets/` (imagens ou prints)
- [ ] README atualizado com resultados e próximos passos

## Evidências (o que colocar no GitHub)
- Trecho do JSON (amostra) e o script de validação
- Lista de 3 achados de qualidade (ex.: colunas com nulos críticos)

## Próximos passos
- Adicionar validações por regra (ex.: faixa de valores, datas no futuro)
- Exportar também um `dados/output/summary.md` (texto legível)

## Créditos
Este projeto faz parte da mentoria **Python para Dados**.
## Como gerar evidências

1- Abra o notebook do entregável  
2- Execute as células até o fim  
3- Faça commit dos arquivos gerados em `assets/`, `reports/` e `outputs/`
