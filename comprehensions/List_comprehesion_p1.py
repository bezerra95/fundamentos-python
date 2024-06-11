
"""
List Comprehensíon

- Utilizando List Comprehension nós podemos gerar novas listas processados a partir de outro
iterável.

# Sintaxe da List Comprehension

[dados for dado iterável]
"""

# Exemplos
'''
numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]  # -> PROCESSA PRA MIN NUMERO VEZES 10
                                           #  PARA CADA NUMERO EM NUMEROS == [10, 20, 30, 40, 50]

print(res) 
'''

"""
Para entender melhor o que está acontecendo devemos divir a expressão em duas partes:

- A primeira parte: for numero in numeros
- A segunda parte: numero * 10

"""
'''
res = [numero / 2 for numero in numeros]
print(res)


def funcao_elevar_aoquadrado(valor):
    return valor * valor


res = [funcao_elevar_aoquadrado(numero) for numero in numeros]

print(res)
'''

# List comprehension veros loop

# Loop
'''
numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []

for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados) == [2, 4, 6, 8, 10]
'''

# List Comprehension
'''
print([numero * 2 for numero in [1, 2, 3, 4, 5]]) == [2, 4, 6, 8, 10]
'''

# Outros Exemplos

# 1
nome = 'Geek University'

print([letra.upper() for letra in nome])


# 2
def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome


amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']
print([caixa_alta(amigo) for amigo in amigos])


# 3
print([numero * 3 for numero in range(1, 10)])


# 4
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])


# 5
print([str(numero) for numero in [1, 2, 3, 4, 5]])