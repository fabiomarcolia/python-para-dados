# Python para Dados — Mentoria (do básico ao avançado)

Repositório de estudo **linear** (do 0 ao avançado), com **trilhas separadas** e entregáveis de **portfólio**.
O foco é ajudar quem já sabe Python básico (e quem vem de Power BI/Excel) a aplicar Python no mundo de **dados**: EDA, visualização, performance e Machine Learning.

## Como estudar (fluxo recomendado)
1- Siga os módulos em ordem: `00_setup` → `01_fundamentos` → ... → `08_machine_learning`
2- Em cada módulo:
- assista/execute o notebook da aula em `notebooks/`
- replique no seu ritmo (15–30 min por aula)
- faça o mini-projeto do módulo em `projects/`
3- Publique no GitHub: notebooks + README do projeto + prints/figuras em `assets/`

## Trilhas (escolha seu foco)
- **Trilha EDA**: `03_pandas` → `04_visualizacao` → `07_eda_avancado`
- **Trilha Performance**: `05_polars` → `06_pyarrow_parquet` → `07_eda_avancado`
- **Trilha ML**: `07_eda_avancado` → `08_machine_learning`

## Setup rápido (VS Code + venv)
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt

# (opcional) registrar kernel do notebook
python -m ipykernel install --user --name python-dados-mentoria
```

## Dados do curso
Este repo usa datasets do repositório abaixo (como fonte):
```bash
git submodule add https://github.com/fabiomarcolia/bases-dados-analytics-powerbi-ml data/source/bases-dados-analytics-powerbi-ml
```

Alternativa (sem submodule):
```bash
git clone --depth 1 https://github.com/fabiomarcolia/bases-dados-analytics-powerbi-ml data/source/bases-dados-analytics-powerbi-ml
```

> Observação: não commite dados pesados em `data/processed` (veja `.gitignore`).

## Estrutura
- `notebooks/` aulas (explicação + prática)
- `scripts/` versões `.py` com **código comentado**
- `projects/` mini-projetos por módulo (portfólio)
- `templates/` checklist e modelos (EDA, README de projeto)
- `data/` dados (fonte via submodule/clone + saídas locais)

## Licença
Defina a licença que preferir (MIT é um bom padrão para material educacional).
