"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.
"""
# Biblíoteca para trabalhar com dados estatíscos
import statistics

# Dados coletados de algum sensor
"""
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
"""
# Calculando a média dos dados utilizando a função mean()
"""
media = statistics.mean(dados)

print(f'Media {media}')
"""
# OBS: Assim como na função map(), após serem utilizadas os dados de filter() recebe dois parâmetros, sendo
# uma função e um iterável.
"""
res = filter(lambda valor: valor > media, dados)
print(list(res))
"""
# OBS: Assim como na função map(), após serem utilizados os dados de filter() eles são excluídos da memória.


paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

print(paises)

# Forma 1
"""
res = filter(None, paises)
print(list(res))
"""

# Forma 2
"""
res = filter(lambda pais: pais > 0, paises)
print(list(res))
"""

# Forma 3
"""
res = filter(lambda pais: pais != '', paises)
print(list(res))
"""

# A Diferença entre map() e filter() é:

# map() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para cada elemento do iterável.

# filter() -> Recebe dois parâmetros, uma função e um iteravel e retorna um objeto filtrando os elementos de acordo com a função.


# Exemplo mais complexo

usuarios = [
    {"username": "Samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "Carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]
print(usuarios)

# Filtrar usuários que estão inativos no Twitter

# Forma 1
#inativos = list(filter(lambda usuario: len(usuario["tweets"]) == 0, usuarios))

# Forma 2
#inativos = list(filter(lambda usuario: not usuario["tweets"], usuarios))
#print(inativos)

# Combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)


