# ✅Configurando Python no VSCode + GitHub

Este repositório tem como objetivo ajudar iniciantes a configurarem um ambiente completo de desenvolvimento Python com o Visual Studio Code (VSCode), incluindo ambiente virtual, instalação de pacotes e integração com GitHub.

## Índice

1. [Introdução](#1-Introdução)  
2. [Instalação do Python](#2-instalação-do-python)  
3. [Instalação do VSCode](#3-instalação-do-vscode)  
4. [Configuração do VSCode para Python](#4-configuração-do-vscode-para-python)  
5. [Criação do Ambiente Virtual](#5-criação-do-ambiente-virtual)  
6. [Instalação de Pacotes Essenciais](#6-instalação-de-pacotes-essenciais)  
7. [Execução e Depuração de Código](#7-execução-e-depuração-de-código)  
8. [Instalação e Configuração do Git](#8-instalação-e-configuração-do-git)  
9. [Integração com GitHub](#9-integração-com-github)  
10. [Recursos Adicionais](#10-recursos-adicionais)

---

## 1. Introdução

Python é uma linguagem de programação de alto nível para programação de propósito geral.

O nome da linguagem de programação Python deriva de uma série de comédia britânica, Monty Python's Flying Circus. A primeira versão foi lançada em 20 de fevereiro de 1991. 

Este repositório ajudará você a aprender Python, principalemnte para o focando na de dados. 

### 💬Por que aprender Python

É uma linguagem de programação muito próxima da linguagem humana e, por isso, fácil de aprender e usar. 

Python é usado por diversos setores e empresas (incluindo o Ele tem sido usado para desenvolver aplicativos web, aplicativos desktop, administração de sistemas e bibliotecas de aprendizado de máquina. 

Python é uma linguagem altamente aceita na comunidade de ciência, análise, engenharia de dados.

Espero que isso seja suficiente para convencê-lo a começar a aprender Python. Python está dominando o mundo, agora com IA!


### Básico da Linguagem
Sintaxe:

Um script Python pode ser escrito no shell interativo Python ou no editor de código. O arquivo terá a extensão .py.

#### Indentação:

Indentação é um espaço em branco em um texto. Algumas linguagens usam para aumentar a legibilidade, o Python usa indentação para criar blocos de código. Assim, um dos erros ao escrever código Python é não usar identação corretamente.

#### Comentários:

Os comentários tem uma função importante para melhorar a legibilidade e permitir que os desenvolvedores deixem informações no código. No Python, qualquer trecho que inicia com #, não é executado e é interpretado como um comentário.

Exemplos de Comentários por linha
```bash
# Esse é um comentário
# Esse é outro comentário
```

#### Comentário de várias linhas

Use aspas triplas entre a parte que é comentário, no inicio e fim:

```bash
"""
Aqui começa a parte comentada.
Pode ser várias linhas a seguir.
Depois é só terminar novamente com aspas triplas
"""
```

Vamos começar montar o ambiente🚀

---

## 2. Instalação do Python

- Acesse: https://www.python.org/downloads 
![Site](https://github.com/fabiomarcolia/python-para-dados/blob/main/img/python_download.png) 
- Baixe a versão mais recente  
- Marque a opção **"Add Python to PATH"**  
- Verifique no terminal:

```bash
python --version
```

---

## 3. Instalação do VSCode

- Acesse: https://code.visualstudio.com/  
- Baixe e instale o VSCode no seu sistema operacional  
- Após a instalação, abra o VSCode normalmente
![VSCode](https://github.com/fabiomarcolia/python-para-dados/blob/main/img/vscode_open.png) 

---

## 4. Configuração do VSCode para Python


- No VSCode, vá até a aba de extensões (ícone de quadrado no menu lateral ou `Ctrl+Shift+X`)  
- Busque por **Python** (desenvolvido pela Microsoft) e clique em instalar  
![Install Python](https://github.com/fabiomarcolia/python-para-dados/blob/main/img/vscode_python_install.png) 
- Após instalar, pressione `Ctrl+Shift+P`, digite `Python: Select Interpreter` e selecione o interpretador desejado

### Instalando Extensões úteis e essenciais

No VS Code, as extensões são ferramentas adicionais que expandem as funcionalidades do editor, permitindo que você personalize o ambiente de desenvolvimento e adicione recursos como suporte a linguagens específicas, formatadores de código, temas e muito mais. Elas são como plugins que se "encaixam" ao programa principal, tornando o VS Code mais versátil e adaptado às suas necessidades. 

Como as extensões funcionam:

- Adicionam recursos
- Personalizam o ambiente:
- Simplificam o trabalho:
- Estão disponíveis no Marketplace:
- Temas: Extensões que mudam o visual do VS Code, com diferentes cores, fontes e estilos. 
- Extensões que adicionam recursos como visualização de conteúdo de portais (Power Apps), lembretes no código (Bookmarks) e muito mais.

### Extensões Recomendadas
  Acesse a aba de extensões no VSCode (Ctrl + Shift + X).
    
- Python (Microsoft): Suporte a Python, Jupyter e IntelliSense.
  
- Jupyter: Permite executar notebooks .ipynb no VSCode.

- Pylance: Melhor análise de código e autocomplete.

- GitLens: Facilita o trabalho com GitHub.

- Code Runner: Executa códigos diretamente no terminal.

- Prettier: Para formatar código.

- Material Icon Theme: Melhora os ícones de arquivos.


---

## 5. Criação do Ambiente Virtual

Abra o terminal integrado (Ctrl + ') e execute:

```bash
mkdir meu-projeto
cd meu-projeto
python -m venv venv
```

Ative o ambiente virtual:

```bash
# Windows
.\venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```



Ambientes virtuais em Python são pastas que contêm uma cópia isolada do interpretador Python e de suas bibliotecas, permitindo que projetos diferentes utilizem versões distintas de pacotes sem conflitos. 

Eles são usados para isolar projetos e garantir que as dependências de um projeto não afetem as de outro, permitindo:

-Isolamento:
Cada ambiente virtual tem seu próprio conjunto de bibliotecas, independentemente do restante do sistema Python. 

Versões de Pacotes:
Permite que um projeto use uma versão específica de um pacote sem conflitos com outros projetos que usam versões diferentes. 

-Gerenciamento de Dependências:
Facilita o gerenciamento de dependências de um projeto, garantindo que ele funcione corretamente com as bibliotecas necessárias. 
Criação:
São criados usando o comando venv ou virtualenv. 

Como funcionam:

1-Criação do Ambiente:
Um ambiente virtual é criado em uma pasta específica do seu projeto, contendo uma cópia do interpretador Python e um sistema de gerenciamento de pacotes (como pip). 

2-Ativação:
Para usar um ambiente virtual, você precisa ativá-lo, geralmente executando um script de ativação (como activate no Windows ou source activate no Linux/macOS). 

3-Instalação de Pacotes:
Após ativar o ambiente, você pode instalar pacotes usando pip como de costume, mas esses pacotes serão instalados apenas nesse ambiente virtual específico. 

4-Desativação:
Para voltar a usar o ambiente Python global, você desativa o ambiente virtual, geralmente executando um comando como deactivate. 

Por que usar:
Evitar Conflitos: Permite que projetos usem versões diferentes de pacotes sem conflitos. 

Reproducibilidade: Garante que seu projeto funcione consistentemente em diferentes ambientes. 

Organização: Facilita a organização de projetos e a gestão de dependências. 

Ferramentas:
venv:
Um módulo padrão do Python para criar ambientes virtuais, especialmente recomendado para versões mais recentes do Python (3.3 e posteriores).
virtualenv:
Uma ferramenta popular para criar ambientes virtuais, compatível com versões mais antigas do Python. 

---

## 6. Instalação de Pacotes Essenciais

Com o ambiente ativado, no terminal:

```bash
pip install pandas numpy matplotlib jupyter
```

Para salvar os pacotes instalados:

```bash
pip freeze > requirements.txt
```


---

## 7. Execução e Depuração de Código

- Crie um arquivo `main.py`  
- Escreva seu código Python  
- Para executar, pressione `Ctrl+F5`  
- Para debugar, pressione `F5`

---

## 8. Instalação e Configuração do Git

- Baixe e instale o Git: https://git-scm.com/downloads  
- Configure seu nome e e-mail no terminal:

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

---

## 9. Integração com GitHub

Inicie o repositório Git:

```bash
git init
git add .
git commit -m "Primeiro commit"
```

Conecte ao repositório remoto no GitHub:

```bash
git remote add origin https://github.com/seuusuario/nomedorepositorio.git
git push -u origin main
```

---

## 10. Começando a usar o VSCode

Abra o VSCode. Ao abri-lo, você verá a interface abaixo:
![](https://github.com/fabiomarcolia/python-para-dados/blob/main/img/vscode_project1.png.png) 


Crie uma pasta chamada AprenderPython30dias na área de trabalho, assim poderá abrir e adicionar ela no VSCode:
![1](https://github.com/fabiomarcolia/python-para-dados/blob/main/img/vscode_project2.png.png)


Agora você verá atalhos para criar arquivos e pastas dentro do diretório do projeto. Veja o exemplo abaixo:
![](https://github.com/fabiomarcolia/python-para-dados/blob/main/img/vscode_project3.png.png)

Pronto, você já poderá usar Python e criar projetos, o ambiente está preparado🚀

## 11. Recursos Adicionais

- [Documentação oficial do Python](https://docs.python.org/pt-br/3/)  
- [Guia oficial do VSCode para Python](https://code.visualstudio.com/docs/python/python-tutorial)  
- [Documentação do Git](https://git-scm.com/doc)  
- [Guia GitHub para iniciantes](https://docs.github.com/pt/get-started)

---

Feito com 🩵 para amantes do Python.

## 🔗 Fale Comigo

[![Linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=black)](https://www.linkedin.com/in/fabiomarcolia/)

[![Mais Recursos](https://github.com/fabiomarcolia/python-para-dados/blob/main/img/topmate.png)](https://topmate.io/fabiomarcolia)






## Autor

- [Fabio Marçolia](https://github.com/fabiomarcolia)

