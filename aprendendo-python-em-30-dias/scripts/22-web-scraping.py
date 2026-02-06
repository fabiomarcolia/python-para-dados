# ============================================
# Tópico: Web Scraping em Python
# Bibliotecas: requests + BeautifulSoup
# Autor: Fabio Marçolia
# ============================================

# --------------------------------------------
# 1. O que é Web Scraping?
# --------------------------------------------
# É a técnica de extrair dados de sites automaticamente.
# Ex: buscar preços, notícias, conteúdos de uma página HTML.

import requests
from bs4 import BeautifulSoup

# --------------------------------------------
# 2. Fazer uma requisição HTTP com requests
# --------------------------------------------
url = "https://quotes.toscrape.com/"  # site de teste com frases
resposta = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if resposta.status_code == 200:
    print("Requisição bem-sucedida!")
else:
    print("Erro ao acessar a página.")

# --------------------------------------------
# 3. Analisar o HTML com BeautifulSoup
# --------------------------------------------
html = resposta.text
soup = BeautifulSoup(html, "html.parser")

# --------------------------------------------
# 4. Extrair informações da página
# --------------------------------------------
# Vamos capturar todas as citações (quotes) e seus autores

quotes = soup.find_all("div", class_="quote")

print("\nFrases encontradas na página:\n")
for q in quotes:
    frase = q.find("span", class_="text").text
    autor = q.find("small", class_="author").text
    print(f"{frase} — {autor}")

# --------------------------------------------
# 5. Extras: Navegar por páginas
# --------------------------------------------
# Esse site tem botão "Next →" com paginação
# Você pode capturar o link da próxima página assim:

next_page = soup.find("li", class_="next")
if next_page:
    proxima_url = "https://quotes.toscrape.com" + next_page.a["href"]
    print("\nLink da próxima página:", proxima_url)

# --------------------------------------------
# Dicas para scraping real:
# --------------------------------------------
# - Sempre verifique os Termos de Uso do site
# - Use headers para simular um navegador:
#     headers = {"User-Agent": "Mozilla/5.0"}
# - Evite requisições em excesso (use time.sleep)
# - Para sites com JavaScript, use Selenium ou Playwright

# --------------------------------------------
# Desafio:
# Crie um scraper para extrair apenas as frases que
# contêm a palavra "life"
