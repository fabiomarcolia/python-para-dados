# ============================================
# Tópico: Ambiente Virtual em Python
# Ferramenta: venv (nativo do Python)
# Autor: Fabio Marçolia
# ============================================

# --------------------------------------------
# O que é um ambiente virtual?
# --------------------------------------------
# É uma forma de isolar as bibliotecas usadas por um projeto,
# evitando conflitos entre versões de pacotes diferentes.

# --------------------------------------------
# 1. Criar um ambiente virtual
# --------------------------------------------
# No terminal (Windows, Linux ou macOS):

# python -m venv venv

# Isso cria uma pasta chamada "venv" com um Python isolado

# --------------------------------------------
# 2. Ativar o ambiente virtual
# --------------------------------------------

# No Windows (cmd ou PowerShell):
# venv\Scripts\activate

# No macOS/Linux:
# source venv/bin/activate

# Após ativar, você verá algo como:
# (venv) C:\seu\projeto>

# --------------------------------------------
# 3. Instalar pacotes no ambiente virtual
# --------------------------------------------
# pip install pandas requests

# Eles serão instalados apenas dentro do ambiente

# --------------------------------------------
# 4. Ver pacotes instalados
# --------------------------------------------
# pip list

# --------------------------------------------
# 5. Criar um arquivo requirements.txt
# --------------------------------------------
# pip freeze > requirements.txt

# Gera um arquivo com todas as versões exatas dos pacotes

# --------------------------------------------
# 6. Instalar a partir do requirements.txt
# --------------------------------------------
# pip install -r requirements.txt

# --------------------------------------------
# 7. Desativar o ambiente virtual
# --------------------------------------------
# deactivate

# Isso retorna ao Python global do sistema

# --------------------------------------------
# Dica bônus: usar com VS Code
# --------------------------------------------
# - Crie o ambiente na raiz do projeto
# - Ative com Ctrl+Shift+P → “Python: Select Interpreter”
# - Escolha o Python da pasta venv

print("Esse script explica o uso de ambiente virtual. Execute os comandos no terminal.")
