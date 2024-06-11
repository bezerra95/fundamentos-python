"""
Map

Com map, fazemos mapeamento de valores para função.
"""

import math

def area(r):
    """Calcula a área de um circulo com raio 'r'."""
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))


raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum
"""
areas = []
for r in raios:
    areas.append(area(r))
print(areas)

"""
# Forma 2 - map
# Map é uma função que recebe dois parâmetros: o primeiro a FUNÇÃO, o segundo um ÍTERÁVEL. Retorna um Map object
"""
areas = map(area, raios)
print(areas)
print(type(areas))

print(list(areas))

"""
# Forma 3 - Map com Lambda
"""
print(list(map(lambda r: math.pi * (r ** 2), raios)))
"""
"""
#OBS: Após utilizar a função map() depois da primeira utilização do resultado, ele zera.
"""

# Para fixar - Map

# Temos dados iteráveis:

# dados: a1, a2, ..., an

# Temos uma função:

# Função: f(X)

# Utilizamos a função map(f, dados) onde map irá 'mapear' cada elemento dos dados e aplicar a função.

# O Map Object: f(a1), f(a2), f(...), f(an)


# Mais um exemplo
# LISTA DE CIDADES E TEMPERATURAS QUE ESTÃO EM GRAUS.
cidades = [('Berlim', 29), ('Caíro', 36), ('Buenos Aíres', 19), ('Los Angeles', 26),
           ('Tokio', 27), ('Nova York', 28), ('Londes', 22)]
print(cidades)

# LISTA DE CIDADES, QUE TEMPERATURAS ESTÃO SENDO TRANFORMADAS EM FAHRENHEIT.
c_para_f = lambda dados: (dados[0], (9 / 5) * dados[1] + 32)
print(list(map(c_para_f, cidades)))
