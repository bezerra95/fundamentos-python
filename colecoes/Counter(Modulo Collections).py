"""
Módulo Collections - Counter

Collections -> High-performance Container Datatypes

Collections -> Recebe um interável como parâmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade
de ocorrências desse elemento.
"""

# Realizando o import

from collections import Counter

# Exemplo 1
# Podemos utilizar qualquer iterável, aqui usamos Lista
'''
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]
'''
# Utilizando o Counter
'''
res = Counter(lista)

print(type(res))

print(res)
# = Counter({1: 5, 3: 5, 2: 4, 5: 4, 4: 3, 45: 2, 66: 2, 43: 1, 34: 1})
'''
# Veja que, para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências.

# Exemplo 2
'''
print(Counter('Geek University'))
# = Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})
'''

# Exemplo 3

texto = """ é uma canção da cantora americana Madonna (imagem), contida em seu décimo primeiro álbum de estúdio, Hard Candy (2008). 
Conta com a participação vocal dos cantores compatriotas Justin Timberlake e Timbaland e foi composta pelos três juntamente com Danja, 
sendo produzida por Timberlake, Timbaland e Danja. O desenvolvimento da faixa foi motivado por um senso de urgência em salvar o planeta 
da destruição, e como as pessoas podem se divertir neste processo. A composição foi concluída através de discussões entre Madonna e 
Timberlake sobre diferentes situações, problemas e relacionamentos. De acordo com a cantora, a música inspirou a produção de seu documentário, 
I Am Because We Are (2008)."""

palavras = texto.split()

# print(palavras)

res = Counter(palavras)

print(res)

# Encontrando as 5 palavras com mais ocorrências no texto
print(res.most_common(5))