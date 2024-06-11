"""
O bloco with

passo para se trabalhar com arquivo

# 1 - Abrimos o arquivo
# 2 - Manipulamos o arquivo
# 3 - Fechamos o arquivo

O bloco with é utilizado para criar um contexto de trabalho onde os recursos
utilizados são fechados após o bloco with.

arquivo - open('leitura_de_arquivo_exemplo.txt')
"""

# O bloco with - Forma Pythônica de manipular arquivds

with open('leitura_de_arquivo_exemplo.txt') as arquivo:
    print(arquivo.readlines())
    # confirmando que o arquivo ainda está aberto, ainda saiu do bloco
    print(arquivo.closed)

# confirmando que o arquivo foi fechado depois que saiu do bloco.
print(arquivo.closed)

