"""
Sorted

OBS: Não confunda, apesar do nome, com a função sort() que já estudamos em listas.
O sort() só funciona em listas.

Podemos utilizar o sorted() com qualquer iterável.

Como o propio nome diz, sorted() serve para ordenar.

OBS: O Sorted, SEMPRE retorna uma LISTA com os elementos do iterável ordenados
"""

# Exemplo
"""
numeros = {6, 1, 8, 2}
print(numeros)

print(sorted(numeros))  # Ordenar do menor para o maior

print(numeros)
"""
"""
numeros = [6, 1, 8, 2]
print(numeros)
print(sorted(numeros))
"""
# Adicionando parâmetros ao sorted()
"""
print(sorted(numeros, reverse=True))  # Oderna do maior para o menor
"""

# Podemos utilizar sorted() para coisas mais complexas
"""
usuarios = [
    {"username": "Samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "Carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": [], "cor": "amarelo"},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": [], "cor": "preto", "musica": "rock"}
]
print(usuarios)
"""
# Ordenando por username - Ordem Alfabética
"""
print(sorted(usuarios, key=lambda usuario: usuario["username"]))
"""
# Ordenando pelo numero de tweets
"""
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))
"""

# Ultimo exemplo

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock'in'roll, too ynoung to die", "tocou": 32}
]
# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordena da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))

