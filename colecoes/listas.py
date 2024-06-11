"""
Listas em Python funciona como vetores/matrizes (arrays) em outras linguagens,
com a diferença de serem DINÁMICO e também de podermos colocar QUALQUER TIPO DE DADO.

- Dinámico: Não possui tamanho fixo: Ou seja, podemos criar a lista e simplesmente ir
adicionando elementos;
- Qualquer tipo de dado: Não Possuem tipo de dado fixo; ou seja,
podemos colocar qualquer tipo de dado.

As Listas são representados por colchetes: []

"""

'''
type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')
'''

#Podemos facilmente checar se determinado valor está contido na lista
"""
num = 7
if num in lista4:
    print(f'Encontrei o numero {num}')
else:
    print(f'Não encontrei o número {num}')
"""


#Podemos facilmente ordenar uma lista
"""
lista1.sort()
print(lista1)

#Podemos facilmente contar o numero de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))
"""


# Adicionar elementos em listas
#Para adicionar elementos em listas, utilizamos a função append
"""
print(lista1)
lista1.append(42)
print(lista1)
"""
# OBS: Com append, nós só conseguimos adicionar 1 elemento por vez
# lista1.append(12, 34, 56) # ERRO
"""
lista1.append([8, 3, 1])
print(lista1)

if [8, 3, 1] in lista1:
    print('Encontrei a Lista')
else:
    print('Não encontrei a lista')
"""


# Coloca cada elemento da lista como valor adicional á lista
"""
lista1.extend([123, 44, 67])
print(lista1)
"""


# Podemos inserir um novo elemento na lista informando a pasição do indice
#OBS: Isso não substitui o valor inicial. O mesmo será deslocado para a direita da lista.
"""
lista.insert(2, Novo Valor')
"""


# Podemos facilmente juntar duas listas
#Forma 1
"""
lista1 = lista1 + lista2
"""
#Forma 2
# lista1.excented(lista2)
"""
print(lista1)
"""


#Podemos facilmente inverter uma lista
#  Forma 1
"""
lista.reverse()
lista2.reverse()
"""
# Forma 2
"""
print(lista1[::-1])
print(lista2[::-1])
"""


#Copiar Lista
"""
lista6 = lista2.copy()
print(lista6)
"""


#Podemos contar quantos elementos existem dentro da lista
"""
print(len(lista5))
"""


#Podemos facilmente remover o último elemento de uma lista
# OBS: O pop não somente remove o último elemento mas também retorna
"""
print(lista5)
lista5.pop()
print(lista5)
"""


#Podemos remover um elemento pelo índice
# OBS: Os elementos á direita deste índice serão deslocados para a esquerda.
# Obs: Se não houver elemento no índice informado, teremos o erro IndexError
"""
lisra5.pop(2)
print(lista5)
"""


# Copiar uma lista
'''
lista6 = lista2.copy()
print(lista6)
'''


#Podemos remover todos os elementos (zerar a lista)
'''
print(lista5)
lista5.clear()
print(lista5)
'''


# Podemos facilmente repetir elementos em uma lista
'''
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)
'''


# Podemos facilmente converter uma string para uma lista
# exemplo 1
'''
curso = 'Programação em python: Essencial'
print(curso)
curso = curso.split()
print(curso)
'''
# OBS: Por padrão, o split separa os elementos da lista pelo espaço entre elas.
'''
#Exemplo 2
curso = 'Programação,em,Python:,Essencial'
print(curso)
curso = curso.split()
'''


#Convertando listas em uma string
#Abaixo estamos falando: Pega a lista6, coloca espaço entre cada elemento e transfomarma em uma string
'''
#Exemplo 1
lista6 = ['Programação', 'em', 'Python:', 'Essencial']
curso = ' '.join(lista6)
print(lista6)

#Exemplo 2
lista6 = ['Programação', 'em', 'Python:', 'Essencial']
curso = '$'.join(lista6)
print(curso)
'''


#Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive esses misturando dados
'''
lista7 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 45345345345]
print(lista7)
print(lista7)
print(type(lista7))
'''


#Iterando sobre listas
#Exemplo 1 - Utilizando for
'''
soma = 0
for elemento in lista4:
    print(elemento)
    doma = soma + elemento
print(soma)
'''
#Exemplo 2 - Utilizando while
'''
carrinho = []
produto = ''

while produto != 'sair'
     print(" Adicione um produto na lista, ou digite 'sair' para sair: ")
     produto = input()
     if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho
    print(produto)
'''


#Utilizando variáveis em listas
'''
#Exemplo 1
numeros = [1, 2, 3, 4, 5]
print(numeros)

#Exemplo 2
num1 = 1
num2 = 2 
num3 = 3
num4 = 4
num5 = 5
print(numeros)
'''


#Fazemos acesso aos elementos de forma indexada

# indices   0         1        2        3
'''
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0])   VERDE
print(cores[1])   AMARELO
print(cores[2])   AZUL
print(cores[3])   BRANCO
'''
# Podemos fazer acessoa aos elementos de forma indexada inversa
# para enetender melhor o indice negativo, PENSE NA LISTA COMO UM CÍRCULO, onde
# o final de um elemento está ligado ao inicio da lista
'''
print(cores[-1])  BRANCO
print(cores[-2])  AZUL
print(cores[-3])  AMARELO
print(cores[-4])  VERDE
#print(cores[-5]) #ERRO, pois não existe índice -5
'''
#LOOPS
'''
cores = ['verde', 'amarelo', 'azul', 'branco']
for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1
'''


# Podemor Gerar indice em for
'''
for indice, cor in enumerate(cores):
    print(indice, cor)
'''


# listas aceitam valores repetidos
'''
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)

print(lista)
'''


#Outros métodos não tão importantes mas também uteis
#Encontrar o indíce de um elemento na lista
'''
numeros = [5, 6, 7, 8, 9, 10]
#Em qual índice da lista está o valor 6?
print(numeros.index(6))

#Em qual índice da lista está o valor 9?
print(numeros.index(9))
'''
#OBS: Caso não tanha este elemento na lista, será apresentado erro ValueError

#Podemos fazer busca dentro de um range a partir do indice
'''
# EXEMPLO
numeros = [5, 6, 7, 5, 8, 9, 10]
print(numeros.index(5, 1) # buscando a partir do indice 1
print(numeros.index(5, 2) # buscando a partir do indice 2
print(numeros.index(5, 3) # buscando a partir do indice 3
Etc...
'''
'''
#Podemos fazer busca dentro de um range, inicio e fim
print(numeros.index(8, 3, 6)) #Buscar o indice do valor 8, entre os indices 3 a 6
'''

#Revisão de slicing

#lista[inicio:fim:passo]
#range(inici:fim:passo]

#Trabalhando com slice de lista com o parâmetro 'inicio'
'''
lista = [1, 2, 3, 4]

print(lista[1:])# Iniciando no índice 1 e pegando todos os elementos resantes
print(lista[::])# Pego todos os elemntos
'''
#Trabalhando com slice de lista com o parâmetro 'fim'
'''
print(lista[:2]) # começa do 0, pega até o indice 2  - 1
print(lista[:4]) # começa em 0, pega até o indice 4  - 1
print(lista[1:3]) # começa em 1, pega até o indice 3  - 1
'''
#Trabalhando com slice de lista com o parâmetro 'passo'
'''
print(lista[1::2]) # Começa em 1,vai até o final, de 2 em 2
print([lista[::2]) # começa em 0,vai até o final, de 2 em 2
'''

#Invertendo valores em uma lista
 #Exemplo 1
'''
nomes = ['Geek', 'University']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)
'''
 #Exemplo 2
'''
nomes = ['Geek', 'University']
nomes.reverse()
print(nomes)
'''


# Soma*, Valor Maximo*, Valor Minimo*, Tamanho da lista
# * Se os valores forem todos inteiros ou reais.
'''
lista = [1, 2, 3, 4, 5, 6]

print(sum(lista)) # soma
print(max(lista)) # máximo valor
print(min(lista)) # minimo valor
print(len(lista)) # tamanho da lista
'''

#Transformar lista em tupla
'''
lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))
'''

# Desempacotamento de listas
'''
lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)
#OBS: SE TIVERMOS NUMEROS DIFERENTES DE ELEMENTOS NA LISTA OU VARIÁVEIS PARA RECEBER OS DADOS, TEREMOS ValueError
'''

# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Forma 1 - Deep copy
lista = [1, 2, 3]
print(lista)
nova = lista.copy()
print(nova)

nova.append(4)
print(lista)
print(nova)
# OBS: Veja que ao utilizarmos lista.copy() copimos da lista para uma nova lista, mas elas
# ficaram totalmente independentes, ou seja, modificando uma lista, não afeta a outra. Isso em Python
# é chamado de Deep Copy (Copia profunda)

# Forma 2 - Shallow Copy
lista = [1, 2, 3]
print(lista)
nova = lista  # cópia
print(nova)

nova.append(4)
print(lista)
print(nova)
# OBS: Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista, mas
# após realizar modificação em uma das listas, essa modificação se refletiu em ambas as listas.
# Isso em Python é chamado de Shallow Copy