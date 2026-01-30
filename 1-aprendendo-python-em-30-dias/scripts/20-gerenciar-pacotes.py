# ============================================
# Tópico: Gerenciador de Pacotes em Python
# Ferramenta principal: pip
# Autor: Fabio Marçolia
# ============================================

# --------------------------------------------
# O que é um gerenciador de pacotes?
# --------------------------------------------
# Um gerenciador de pacotes permite:
# - Instalar bibliotecas de terceiros (ex: pandas, requests)
# - Remover, atualizar e listar pacotes
# - Gerenciar dependências do seu projeto

# --------------------------------------------
# 1. Instalar pacotes com pip
# --------------------------------------------
# Execute no terminal ou no Jupyter:

# pip install nome_do_pacote

# Exemplo:
# pip install pandas

# --------------------------------------------
# 2. Importar e usar pacotes instalados
# --------------------------------------------

import requests  # Só funciona se o pacote estiver instalado

response = requests.get("https://api.github.com")
print("Status da requisição:", response.status_code)

# --------------------------------------------
# 3. Ver pacotes instalados
# --------------------------------------------
# pip list

# --------------------------------------------
# 4. Ver detalhes de um pacote específico
# --------------------------------------------
# pip show pandas

# --------------------------------------------
# 5. Atualizar um pacote
# --------------------------------------------
# pip install --upgrade nome_do_pacote

# --------------------------------------------
# 6. Desinstalar um pacote
# --------------------------------------------
# pip uninstall nome_do_pacote

# --------------------------------------------
# 7. Usar um arquivo requirements.txt
# --------------------------------------------
# Esse arquivo lista os pacotes do projeto com suas versões
# Exemplo do conteúdo:

# pandas==1.5.3
# requests>=2.28

# Para instalar todos os pacotes listados:
# pip install -r requirements.txt

# --------------------------------------------
# 8. Gerar requirements.txt automaticamente
# --------------------------------------------
# pip freeze > requirements.txt

# --------------------------------------------
# 9. Ambiente virtual (virtualenv)
# --------------------------------------------
# Cria um ambiente isolado para instalar pacotes só para um projeto

# python -m venv venv          # cria o ambiente
# source venv/bin/activate     # Linux/macOS
# venv\Scripts\activate        # Windows

# Depois disso, use pip normalmente
# Para desativar: deactivate

# --------------------------------------------
# Dica extra: pipx (executar pacotes como CLI)
# --------------------------------------------
# pipx install pacote-cli
# Exemplo: pipx install jupyterlab

print("\nResumo: pip é essencial para gerenciar bibliotecas externas no Python.")
