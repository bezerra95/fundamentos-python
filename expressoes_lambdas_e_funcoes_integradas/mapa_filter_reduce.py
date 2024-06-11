from pprint import pprint

_print = print()
print = pprint

produtos = [
    {'nome': 'P1', 'preco': 59.90, 'peso_kg': 1.312, 'variacoes': ['a', 'b']},
    {'nome': 'P2', 'preco': 19.55, 'peso_kg': 2.300, 'variacoes': ['c', 'd']},
    {'nome': 'P3', 'preco': 9.13, 'peso_kg': 0.150, 'variacoes': ['e', 'f']},
    {'nome': 'P4', 'preco': 3.49, 'peso_kg': 0.789, 'variacoes': ['g', 'h']},
    {'nome': 'P5', 'preco': 33.22, 'peso_kg': 3.578, 'variacoes': ['i', 'j']},
    {'nome': 'P6', 'preco': 67.79, 'peso_kg': 9.920, 'variacoes': ['k', 'l']},
    {'nome': 'P7', 'preco': 45.31, 'peso_kg': 1.123, 'variacoes': ['m', 'n']},
    {'nome': 'P8', 'preco': 93.27, 'peso_kg': 0.521, 'variacoes': ['o', 'p']},
    {'nome': 'P9', 'preco': 1.90, 'peso_kg': 1.300, 'variacoes': ['q', 'r']},
]


#REDUZA
# preco_total = redução (lambda soma, p: soma + p['preco'], produtos, 0)
# preco_total_list_comprehension = soma ([p['preco'] para p em produtos])
# impressão (preco_total)
# impressão (preco_total_list_comprehension)

# FILTRO
# produtos_filter = lista (filtro(lambda p: p['preco'] > 20, produtos))
# produtos_filter_list_comprehension = [p para p em produtos se p['preco'] > 20]
# impressão (produtos_filter_list_comprehension)

#MAPA
produtos_map = list(map(lambda p: p['preco'], produtos))
produtos_map_list_comprehension = [produto['preco'] for produto in produtos]

print(produtos_map)
print(produtos_map_list_comprehension)

#FORMA NORMAL
# precos = []
# para produto em produtos:
#     precos.append(produto['preco'])