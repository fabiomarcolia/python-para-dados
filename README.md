# Python para Dados | Básico ao Avançado com Mini-Projetos para Portifólio

Repositório **do básico ao avançado** para quem já sabe Python ([Aqui para aprender do zero](aprendendo-python-em-30-dias/README.md)) e quer aplicar em **dados** — com trilha **linear**, trilhas por objetivo e **entregáveis de portfólio** (notebook por módulo).



![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange)
![Pandas](https://img.shields.io/badge/pandas-ready-informational)

![GitHub stars](https://img.shields.io/github/stars/fabiomarcolia/python-para-dados?style=social)
![Last commit](https://img.shields.io/github/last-commit/fabiomarcolia/python-para-dados)

### 🚨 Atenção: se ainda não tiver o ambiente VSCode com Python configurado, dê uma olhada aqui👇
- [Configurando ambiente: VSCode com Python + Github](vscode_python_github.md)

## O que você vai aprender aqui
- EDA completa (limpeza, joins, agregações, narrativa e evidências)
- Visualização: matplotlib, seaborn e plotly
- Performance: polars + pyarrow/parquet
- Consulta local com duckdb (sem “ensinar SQL” como trilha principal)
- ML baseline com scikit-learn (pipeline + métricas)
  

## Roteiro de estudo (como aprender na ordem)

A lógica aqui é: 
- **praticar** → [Notebooks](notebooks)  
- **reforçar** → [Scripts](scripts) 
- **finalizar** → [Mini-Projeto](projetos) 
- **publicar** → [Potifólio](portifolio.md)

  - [Roadmap dessa mentoria Python para Dados](ROADMAP.md)

### Passo a passo por módulo (repetir do 1 ao 9)
1- **Aula (Notebook)**  
   Vá em [notebooks](notebooks) e pratique cada um até se familiarizar completamente (aproximadamente ficará em cada um entre 15 a 30 min cada).

2- **Reforço (Script)**  
   Rode a versão comentada em [scripts](scripts) para fixar sem depender de notebook.

3- **Entregável (Portfólio)**  
   Abra [Entregável Portifólio](projetos/1_setup/1_entregavel_portfolio.ipynb) e execute até o fim.  
   Ele gera evidências dentro do próprio módulo:
   - `projetos/<módulo>/assets/` (imagens/HTML)
   - `projetos/<módulo>/reports/` (Markdown/JSON)
   - `projetos/<módulo>/outputs/` (parquet/modelos)

4- **Publicação (GitHub)**  
   Faça commit das evidências e atualize o README do mini-projeto com 2–3 bullets:
   - o que você fez
   - 1–2 insights
   - onde está a evidência (imagem/relatório)

### Frequência sugerida (semana a semana)
- **Modo acelerado (2 semanas):** 1 módulo por dia útil + revisão no fim de semana
- **Modo sustentável (4–6 semanas):** 2 módulos por semana + 1 dia só para o entregável
- **Modo portfólio (8 semanas):** 1 módulo por semana, caprichando nos assets e no texto do README

### Sugestão para aprender de verdade
- Se travar, **não pule**: finalize o entregável com o dataset .  
- Depois, repita usando outro dataset.

  - [Bases para Treino](dados/bases_treino)


## Conteúdo
- [Setup do ambiente](#começo-rápido)
- [Roteiro de estudo](#roteiro-de-estudo-como-aprender-na-ordem)
- [Estrutura do repositório](#estrutura-do-repositório)
- [Roadmap linear](#roadmap-linear)
- [Trilhas](#trilhas)
- [Progress tracker](#progress-tracker)
- [Portfólio](#portfólio)
- [Datasets](#datasets)
- [Dicas para seu Git](#dicas-para-deixar-seu-github-mais-profissional)

## Começo rápido
1- Clone o repositório:
```bash
git clone https://github.com/fabiomarcolia/python-para-dados.git
cd python-para-dados
```

2- Crie e ative o ambiente virtual:
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate
```

3- Instale dependências:
```bash
pip install -r requirements.txt
```

4- Abra no VS Code e rode os notebooks:
- `notebooks/` (aulas)
- `projetos/<módulo>/01_entregavel_portfolio.ipynb` (entregável de portfólio)

## Estrutura do repositório
- `1_setup/` a `9_machine_learning/` (linha do Zero ao avançado)
- `notebooks/` aulas com explicação + prática (15–30 min)
- `scripts/` versões `.py` comentadas (para rodar sem notebook)
- `projetos/` mini-projetos por módulo + entregáveis de portfólio
- `templates/` checklist e templates (EDA e README)
- `dados/`
  - `sample/` dataset pequeno (sempre roda)
  - `source/` datasets reais (opcional)

## Roadmap
Veja a sequência completa em: [`ROADMAP.md`](./ROADMAP.md)

## Trilhas
- **Trilha EDA**: pandas → visualização → EDA avançado
- **Trilha Performance**: polars → pyarrow/parquet → EDA avançado
- **Trilha ML**: EDA avançado → scikit-learn (baseline)

## Acompanhar Progresso
Use o índice de portfólio para acompanhar entregáveis por módulo:
- [`portifolio.md`](./portifolio.md)

## Portfólio
O repo foi pensado para você gerar evidências “publicáveis” no GitHub:

- Cada módulo tem um notebook entregável:
  - `projetos/<módulo>/01_entregavel_portfolio.ipynb`
- Evidências geradas ficam em:
  - `projetos/<módulo>/assets/` (imagens/HTML)
  - `projetos/<módulo>/reports/` (Markdown/JSON)
  - `projetos/<módulo>/outputs/` (parquet/modelos)

Dica: use o projeto final (pasta `projetos/10_projeto_final_end_to_end/`) como peça principal e os mini-projetos como evidência incremental.

## Datasets
Dataset real sugerido (opcional) via submodule:
```bash
git submodule add https://github.com/fabiomarcolia/bases-dados-analytics-powerbi-ml dados/source/bases-dados-analytics-powerbi-ml
```

Se você não adicionar o submodule, tudo roda com os arquivos em `dados/bases_treino/`.

## Dicas para deixar seu GitHub mais profissional

- Use os [projetos](projetos) aqui como referência.
- Use o [modelo de estrutura](recursos_templates_python/modelo-estrutura-novo-projeto) para criar projetos para seu portifólio.
- Coloque uma imagem para o repositório > Settings → Social preview '(imagem 1280×640)
- Crie sua apresentação com um [README](https://docs.github.com/pt/account-and-profile/how-tos/profile-customization/managing-your-profile-readme) do seu perfil 

## Conclusão

Este repositório serve como uma mentoria guiada para aprender Python para dados. Seu aprendizado pode abrir uma janela de oportunidades, atualmente python é usa em várias funções e tecnologia: IA, Data Engineer, Data Analytics, Data Science entre outras.

## Autor - Fabio Marçolia | Carreira em Dados & IA

Para mais conteúdo de Python, Carreira em Dados e IA, ou se quiser falar comigo sobre dúvidas, sugestões ou feedback:

- Linkedin: [Vamos nos conectar e me envie uma mensagem🤝](http://linkedin.com/in/fabiomarcolia)
- Mais Recursos de Carreira: [Veja aqui](https://topmate.io/fabiomarcolia)

Agradeço seu apoio e fique a vontade de entrar em contato comigo!