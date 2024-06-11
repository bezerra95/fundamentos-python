"""
Ranges

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabaçhar melhor com loops for.

Ranges são utilizadaos para gerar sequências numéricas, não de forma aleatória,
mas sim de maneira especificada.

Formas gerais:

# Forma 1
range(valor_de_parada)
OBS: Valor_de_parada não inclusive(inicio padrão é zero, e passo em 1 em 1)
# Exemplo Forma 1
for num in range(11):
    print(num)


#Forma 2
range(valor_de_inicio, valor_de_parada)
OBS: valor_de_parada não inclusive (inicio especificado pelo usuário, e passo de 1 em 1)
# Exemplo Forma 2
for num in range(4, 11)
   print(num)


# Forma 3
range(valor_de_inicio, valor_de_parada, passo)
OBS: valor_de_parada não inclusive (inicio especificado pelo usuário, e passo especificado pelo usuário)
#Exemplo Forma 3
for num in range(5, 55, 5):
   print(num)


# Forma 4 (inversa)
range(valor_de_inicio, valor_de_parada, passo)
OBS: valor_de_parada não inclusive (inicio especificado pelo usuário, e passo especificado pelo usuário)
#Exemplo 4
for num in range(10, -1,-1):
   print(num)


DICA PARA CRIAR UMA LISTA
lista = list(range(11))
  print(lista) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""