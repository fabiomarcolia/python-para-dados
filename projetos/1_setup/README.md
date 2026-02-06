# Mini-projeto — 00_setup — Setup e ambiente no VS Code


Este mini-projeto consolida o módulo **00_setup** em um entregável de **portfólio**.
- Tempo estimado: 15–30 min
- Trilhas: core


## Entregável (portfólio)

- Notebook: [`01_entregavel_portfolio.ipynb`](./01_entregavel_portfolio.ipynb)
- Evidências:
  - `assets/` (imagens/HTML)
  - `reports/` (Markdown/JSON)
  - `outputs/` (parquet/modelos)


## Objetivo
Deixar o repositório 100% executável no VS Code com `.venv`, Jupyter e um fluxo de trabalho consistente.

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
- [`notebooks/00_setup/01_setup_ambiente.ipynb`](../../notebooks/00_setup/01_setup_ambiente.ipynb)
- [`notebooks/00_setup/02_vscode_jupyter_fluxo.ipynb`](../../notebooks/00_setup/02_vscode_jupyter_fluxo.ipynb)

### Scripts
- [`scripts/00_setup/01_setup_ambiente.py`](../../scripts/00_setup/01_setup_ambiente.py)
- [`scripts/00_setup/02_vscode_jupyter_fluxo.py`](../../scripts/00_setup/02_vscode_jupyter_fluxo.py)


## Entregáveis (portfólio)
- Ambiente criado (`.venv`) e dependências instaladas
- Kernel do Jupyter configurado e executando notebooks
- Prints em `assets/` comprovando execução (opcional)

## Checklist de entrega
- [ ] Notebook com narrativa (perguntas → análises → conclusão)
- [ ] Export de artefatos (quando fizer sentido): `dados/processed/` e/ou `dados/output/`
- [ ] Evidências em `assets/` (imagens ou prints)
- [ ] README atualizado com resultados e próximos passos

## Evidências (o que colocar no GitHub)
- Print do notebook executado (célula com import das libs + versão do Python)
- Print do VS Code com kernel selecionado (ou output no terminal)

## Próximos passos
- Adicionar `pre-commit` com lint/format (opcional)
- Criar um atalho no VS Code para rodar scripts com `.venv`

## Créditos
Este projeto faz parte da mentoria **Python para Dados**.
## Como gerar evidências

1- Abra o notebook do entregável  
2- Execute as células até o fim  
3- Faça commit dos arquivos gerados em `assets/`, `reports/` e `outputs/`
