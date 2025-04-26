# ============================================
# Tópico: Classes e Objetos em Python
# Programação Orientada a Objetos (POO)
# Autor: Fabio Marçolia
# ============================================

# --------------------------------------------
# 1. O que são classes e objetos?
# --------------------------------------------
# Classe: molde/estrutura para criar objetos
# Objeto: instância concreta da classe

# --------------------------------------------
# 2. Criando uma classe simples
# --------------------------------------------
class Pessoa:
    # Construtor: chamado quando o objeto é criado
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Método: função que pertence à classe
    def apresentar(self):
        print(f"Olá! Meu nome é {self.nome} e tenho {self.idade} anos.")

# Criando objetos (instâncias)
p1 = Pessoa("Fabio", 30)
p2 = Pessoa("Ana", 25)

p1.apresentar()
p2.apresentar()

# --------------------------------------------
# 3. Atributos públicos e privados
# --------------------------------------------
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # atributo privado

    def exibir_saldo(self):
        print(f"Saldo de {self.titular}: R$ {self.__saldo:.2f}")

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente!")

conta = ContaBancaria("Maria", 1000)
conta.exibir_saldo()
conta.depositar(500)
conta.sacar(300)
conta.exibir_saldo()

# --------------------------------------------
# 4. Herança (subclasse herda de uma classe)
# --------------------------------------------
class Funcionario(Pessoa):  # herda de Pessoa
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade)  # chama o __init__ da superclasse
        self.cargo = cargo

    def apresentar(self):
        print(f"Olá! Sou {self.nome}, {self.cargo}, e tenho {self.idade} anos.")

f1 = Funcionario("Carlos", 35, "Analista de Dados")
f1.apresentar()

# --------------------------------------------
# 5. Métodos especiais: __str__
# --------------------------------------------
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f}"

p = Produto("Notebook", 3999.90)
print(p)

# --------------------------------------------
# Boas práticas:
# - Use nomes significativos
# - Separe responsabilidades em diferentes classes
# - Encapsule dados com atributos privados quando necessário
# - Crie métodos claros, com uma única responsabilidade

# --------------------------------------------
# Desafio:
# Crie uma classe Carro com atributos modelo, ano e cor.
# Inclua um método descrever() que imprime os dados do carro.
