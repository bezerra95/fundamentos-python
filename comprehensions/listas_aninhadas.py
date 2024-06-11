"""
Listas Aninhadas (Nested Lists)

- Algumas Linguagens de programação (C/Java) possuem uma estrutura de dados chamadas de arrays:
   - Unidimensinais (Arrays/Vetores);
   - Multidimensionais (Matrizes);

Em Python nós temos as Listas

numeros = [1, 'b', 3.234, True, 5]

"""

# Exemplos
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3 x 3
print(listas)
print(type(listas))

# Como fazemos para acessar os dados?
print(listas[0])  # = [1, 2, 3]
print(listas[0][1])  # = 2
print(listas[2][1])  # = 8

# Iterando com loops em uma lista aninhada
for lista in listas:
    print(lista)  # = [1, 2, 3]
                  #   [3, 4, 5]
                  #   [6, 7, 8]

for lista in listas:
    for numero in lista:
        print(numero) # = 1 2 3 4 5 6 7 8 9


# List Comprehension
# = Para cada Lista em Listas, e para cada numero em lista imprima numero
[[print(numero) for numero in lista] for lista in listas]


# Outros exemplos
# Gerando um tabuleiro/matrix 3x3
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valor iniciais
print([['*' for numero in range(1, 4)] for valor in range(1, 4)])

