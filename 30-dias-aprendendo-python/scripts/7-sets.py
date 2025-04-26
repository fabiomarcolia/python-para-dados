# Sets em Python
'''
O que são Sets?
Sets (conjuntos) são estruturas de dados em Python que armazenam coleções não ordenadas
de elementos únicos. Semelhantes aos conjuntos matemáticos, não permitem elementos
duplicados e suportam operações como união, interseção e diferença. Sets são mutáveis,
mas seus elementos devem ser imutáveis (como strings, números ou tuplas).
'''

print("=== SETS EM PYTHON ===\n")

# 1. Criando Sets
print("1. CRIANDO SETS")
print("Existem várias maneiras de criar sets em Python.")

# Set vazio (precisa usar a função set(), pois {} cria um dicionário vazio)
set_vazio = set()
print(f"Set vazio: {set_vazio}")

# Set com elementos
numeros = {1, 2, 3, 4, 5}
print(f"Set de números: {numeros}")

# Set a partir de uma lista (elimina duplicatas)
lista_com_duplicatas = [1, 2, 2, 3, 4, 4, 5]
set_sem_duplicatas = set(lista_com_duplicatas)
print(f"Lista original: {lista_com_duplicatas}")
print(f"Set sem duplicatas: {set_sem_duplicatas}")

# Set a partir de uma string (cada caractere se torna um elemento)
set_letras = set("python")
print(f"Set a partir da string 'python': {set_letras}")

# Set com diferentes tipos de dados (elementos imutáveis)
set_misto = {1, "python", 3.14, True, (1, 2)}
print(f"Set com diferentes tipos: {set_misto}")

# 2. Características dos Sets
print("\n2. CARACTERÍSTICAS DOS SETS")

# Não permite duplicatas
set_com_duplicatas = {1, 2, 3, 1, 2, 4}
print(f"Set com duplicatas na criação: {set_com_duplicatas}")  # As duplicatas são eliminadas

# Não é indexável (não suporta acesso por índice)
try:
    valor = numeros[0]  # Isso causará erro
except TypeError as e:
    print(f"Erro ao tentar acessar por índice: {e}")

# Não é ordenado (a ordem dos elementos pode variar)
print(f"A ordem dos elementos não é garantida: {numeros}")

# Elementos devem ser imutáveis
try:
    set_invalido = {1, 2, [3, 4]}  # Isso causará erro
except TypeError as e:
    print(f"Erro ao tentar incluir objeto mutável: {e}")

# 3. Métodos para Adicionar e Remover Elementos
print("\n3. MÉTODOS PARA ADICIONAR E REMOVER ELEMENTOS")

cores = {"vermelho", "verde", "azul"}
print(f"Set original: {cores}")

# Adicionando elementos
cores.add("amarelo")
print(f"Após cores.add('amarelo'): {cores}")

# Tentando adicionar um elemento duplicado
cores.add("vermelho")  # Não causa erro, mas não faz nada
print(f"Após cores.add('vermelho'): {cores}")

# Adicionando múltiplos elementos
cores.update(["laranja", "roxo", "verde"])  # pode ser set, lista, etc.
print(f"Após cores.update(['laranja', 'roxo', 'verde']): {cores}")

# Removendo elementos
cores.remove("roxo")  # Remove um elemento específico
print(f"Após cores.remove('roxo'): {cores}")

try:
    cores.remove("preto")  # Causa erro se o elemento não existir
except KeyError as e:
    print(f"Erro ao tentar remover elemento inexistente: {e}")

# Alternativa segura para remover
cores.discard("preto")  # Não causa erro se o elemento não existir
print(f"Após cores.discard('preto'): {cores}")

# Removendo e retornando um elemento arbitrário
elemento = cores.pop()
print(f"Elemento removido com cores.pop(): {elemento}")
print(f"Set após pop(): {cores}")

# Removendo todos os elementos
cores.clear()
print(f"Após cores.clear(): {cores}")

# 4. Operações com Sets
print("\n4. OPERAÇÕES COM SETS")
print("Sets suportam várias operações matemáticas de conjuntos.")

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(f"Set A: {A}")
print(f"Set B: {B}")

# União (elementos que estão em A OU em B)
uniao = A | B  # ou A.union(B)
print(f"União (A | B): {uniao}")

# Interseção (elementos que estão em A E em B)
intersecao = A & B  # ou A.intersection(B)
print(f"Interseção (A & B): {intersecao}")

# Diferença (elementos que estão em A mas NÃO em B)
diferenca = A - B  # ou A.difference(B)
print(f"Diferença (A - B): {diferenca}")

# Diferença simétrica (elementos que estão em A OU B, mas NÃO em ambos)
diferenca_simetrica = A ^ B  # ou A.symmetric_difference(B)
print(f"Diferença simétrica (A ^ B): {diferenca_simetrica}")

# 5. Métodos para Operações com Sets
print("\n5. MÉTODOS PARA OPERAÇÕES COM SETS")
print("Além dos operadores, existem métodos equivalentes.")

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(f"Set A: {A}")
print(f"Set B: {B}")

# União
print(f"A.union(B): {A.union(B)}")

# Interseção
print(f"A.intersection(B): {A.intersection(B)}")

# Diferença
print(f"A.difference(B): {A.difference(B)}")

# Diferença simétrica
print(f"A.symmetric_difference(B): {A.symmetric_difference(B)}")

# Atualizando o próprio set (métodos in-place)
C = {1, 2, 3, 4, 5}
print(f"Set C original: {C}")

C.update(B)  # União in-place (C = C | B)
print(f"Após C.update(B): {C}")

D = {1, 2, 3, 4, 5}
print(f"Set D original: {D}")

D.intersection_update(B)  # Interseção in-place (D = D & B)
print(f"Após D.intersection_update(B): {D}")

E = {1, 2, 3, 4, 5}
print(f"Set E original: {E}")

E.difference_update(B)  # Diferença in-place (E = E - B)
print(f"Após E.difference_update(B): {E}")

F = {1, 2, 3, 4, 5}
print(f"Set F original: {F}")

F.symmetric_difference_update(B)  # Diferença simétrica in-place (F = F ^ B)
print(f"Após F.symmetric_difference_update(B): {F}")

# 6. Métodos de Comparação de Sets
print("\n6. MÉTODOS DE COMPARAÇÃO DE SETS")

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {6, 7, 8}
print(f"Set A: {A}")
print(f"Set B: {B}")
print(f"Set C: {C}")

# Verificando se um set é subconjunto de outro
print(f"A.issubset(B): {A.issubset(B)}")  # A é subconjunto de B?
print(f"A <= B: {A <= B}")  # Operador equivalente

# Verificando se um set é superconjunto de outro
print(f"B.issuperset(A): {B.issuperset(A)}")  # B é superconjunto de A?
print(f"B >= A: {B >= A}")  # Operador equivalente

# Verificando se dois sets não têm elementos em comum
print(f"A.isdisjoint(C): {A.isdisjoint(C)}")  # A e C são disjuntos?
print(f"A.isdisjoint(B): {A.isdisjoint(B)}")  # A e B são disjuntos?

# 7. Compreensão de Sets (Set Comprehension)
print("\n7. COMPREENSÃO DE SETS (SET COMPREHENSION)")
print("Uma forma concisa de criar sets baseados em sequências existentes.")

# Forma básica
numeros = [1, 2, 3, 4, 5, 5, 4, 3]
quadrados = {x**2 for x in numeros}
print(f"Lista original: {numeros}")
print(f"Set de quadrados (sem duplicatas): {quadrados}")

# Com condição
pares = {x for x in range(10) if x % 2 == 0}
print(f"Set de números pares de 0 a 9: {pares}")

# 8. Frozensets (Sets Imutáveis)
print("\n8. FROZENSETS (SETS IMUTÁVEIS)")
print("Versão imutável dos sets, semelhante à relação entre tuplas e listas.")

# Criando um frozenset
fs = frozenset([1, 2, 3, 4])
print(f"Frozenset: {fs}")

# Não pode ser modificado
try:
    fs.add(5)  # Isso causará erro
except AttributeError as e:
    print(f"Erro ao tentar modificar frozenset: {e}")

# Pode ser usado como elemento em outro set
conjunto_de_frozensets = {frozenset([1, 2]), frozenset([3, 4])}
print(f"Set contendo frozensets: {conjunto_de_frozensets}")

# Ou como chave em um dicionário
dicionario = {frozenset([1, 2]): "conjunto 1-2"}
print(f"Dicionário com frozenset como chave: {dicionario}")

# 9. Casos de Uso Comuns para Sets
print("\n9. CASOS DE USO COMUNS PARA SETS")

# Removendo duplicatas de uma sequência
lista = [1, 2, 2, 3, 3, 3, 4, 5, 5]
lista_sem_duplicatas = list(set(lista))
print(f"Lista original: {lista}")
print(f"Lista sem duplicatas: {lista_sem_duplicatas}")

# Verificação de pertencimento rápida
numeros_grandes = set(range(1000, 2000))
print(f"1500 está em numeros_grandes: {1500 in numeros_grandes}")  # Busca eficiente O(1)

# Encontrando elementos distintos
texto = "python é uma linguagem de programação versátil e poderosa"
caracteres_distintos = set(texto.replace(" ", ""))
print(f"Caracteres distintos no texto: {caracteres_distintos}")
print(f"Quantidade de caracteres distintos: {len(caracteres_distintos)}")

# 10. Performance e Limitações
print("\n10. PERFORMANCE E LIMITAÇÕES")

print("Vantagens dos Sets:")
print("  - Busca muito rápida (operação 'in' é O(1) em média)")
print("  - Eliminação automática de duplicatas")
print("  - Operações de conjunto eficientes")

print("\nLimitações dos Sets:")
print("  - Não mantém ordem dos elementos")
print("  - Não permite acesso por índice")
print("  - Elementos devem ser imutáveis")
print("  - Uso de memória pode ser maior que listas equivalentes")

# 11. Sets vs Listas vs Tuplas: Quando Usar Cada Um
print("\n11. SETS VS LISTAS VS TUPLAS: QUANDO USAR CADA UM")

print("Use Sets quando:")
print("  - Precisa garantir elementos únicos")
print("  - Precisa realizar operações de conjuntos (união, interseção, etc.)")
print("  - A ordem dos elementos não importa")
print("  - Precisa verificar pertencimento de maneira eficiente")

print("\nUse Listas quando:")
print("  - A ordem dos elementos é importante")
print("  - Pode haver elementos duplicados")
print("  - Precisa acessar elementos por índice")
print("  - Precisa de uma sequência que pode ser modificada")

print("\nUse Tuplas quando:")
print("  - Precisa de uma sequência imutável")
print("  - A ordem é importante")
print("  - Precisa usar como chave em dicionários ou elemento em sets")