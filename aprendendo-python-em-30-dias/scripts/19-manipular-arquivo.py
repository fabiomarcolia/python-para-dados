# ============================================
# Tópico: Manipulação de Arquivos em Python
# Autor: Fabio Marçolia
# ============================================

# --------------------------------------------
# 1. Criar e escrever em um arquivo (modo "w")
# --------------------------------------------
# "w" = write → cria ou sobrescreve um arquivo

with open("exemplo.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Linha 1\n")
    arquivo.write("Linha 2\n")
print("Arquivo criado e escrito com sucesso!\n")

# --------------------------------------------
# 2. Ler o conteúdo do arquivo (modo "r")
# --------------------------------------------
# "r" = read → leitura

with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo do arquivo:")
    print(conteudo)

# --------------------------------------------
# 3. Ler linha por linha
# --------------------------------------------
print("\nLendo linha por linha:")
with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())

# --------------------------------------------
# 4. Adicionar conteúdo sem apagar o anterior (modo "a")
# --------------------------------------------
# "a" = append → adiciona conteúdo ao final do arquivo

with open("exemplo.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("Linha 3 adicionada\n")
print("\nNova linha adicionada.")

# --------------------------------------------
# 5. Verificar o conteúdo novamente
# --------------------------------------------
with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
    print("\nConteúdo atualizado:")
    print(arquivo.read())

# --------------------------------------------
# 6. Escrever listas de forma automática com writelines()
# --------------------------------------------
linhas = ["Python é ótimo!\n", "Manipular arquivos é fácil!\n"]

with open("novo_arquivo.txt", "w", encoding="utf-8") as arq:
    arq.writelines(linhas)
print("Arquivo 'novo_arquivo.txt' criado com várias linhas.")

# --------------------------------------------
# 7. Remover um arquivo (modo seguro)
# --------------------------------------------
import os

if os.path.exists("teste_para_remover.txt"):
    os.remove("teste_para_remover.txt")
    print("Arquivo removido.")
else:
    print("Arquivo não existe, nada foi removido.")

# --------------------------------------------
# Dicas de modos de abertura:
# --------------------------------------------
# "r"   → leitura
# "w"   → escrita (sobrescreve)
# "a"   → append (adiciona ao final)
# "r+"  → leitura + escrita
# "w+"  → escrita + leitura (sobrescreve)
# "a+"  → leitura + append

# --------------------------------------------
# Desafio: Crie uma função que leia um arquivo e conte as linhas
# --------------------------------------------
def contar_linhas(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            return len(f.readlines())
    except FileNotFoundError:
        return "Arquivo não encontrado!"

print("\nDesafio: O arquivo 'exemplo.txt' tem", contar_linhas("exemplo.txt"), "linhas.")
