"""
Loop for

Loop -> Estrutura de repetição.
for -> Uma das estruturas.

for item in interável:
    //execusão do loop
-------------------------------------------------------------------------------------------------------------

Utiizamos loop para interar sobre sequências ou sobre valores iteráveis.

Exemplos iteráveis:
- String
    nome = 'Geek University'

-Lista
    lista = [1, 3, 5, 7, 9]

-Range
    numeros = range(1, 10)

    #Exemplo de for 1 (iterando em uma string)
for letra in nome:
    print(letra)

#Exemplo de for 2 (iterando sobre uma lista)
for numero in lista:
    print(numero)

#Exemplo de for 3 (iterando sobre um range)
for numero in range(1, 10):
    print(numero)
---------------------------------------------------------------------------------------------------------------

Enumerate:
( (0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4, ' '), (5, 'U')... )

for indice, letra in enumerate(nome):
     print(nome[indice])

for indice, letra in enumerate(nome):
     print(letra)

OBS: QUANDO NÃO PRECISAMOS DE UM VALOR, PODEMOS DESCARTÁ-LO UTILIZANDO UNDERLINE(_)
for _, letra in enumerate(nome):
     print(letra)
----------------------------------------------------------------------------------------------------------------


nome = 'Geek University'
lista = [1, 2, 5, 7, 9]
numeros = range(1, 10)  #Temos que transformar em uma Lista

for valor in enumerate(nome):
     print(valor)

qtd = int(input('QUANTAS VEZES ESSE LOOP DEVE RODAR?'))
soma = 0

for n in range(1, qtd+1):
     num = int(input(f' informe o {n}/{qtd} valor: '))
     soma = soma + num
print(f'A soma é {soma}' )

for letra in nome:
    print(letra, end='')

Tabela de emoji unicode: https://apps.timwhitlock.info/emoji/tables/unicode
-------------------------------------------------------------------------------------------------------------
"""

# Original: U+1F605
# Modificado: U0001F605

for _ in range(3):
    for num in range(1, 11):
        print('\U0001F605' * num)



