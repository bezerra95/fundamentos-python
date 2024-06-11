"""
Seek e Cursors

seek() -> É utilizada para movimentar o cursor pelo arquivo.
"""

# Exemplo 1
'''
arquivo = open('leitura_de_arquivo_exemplo.txt')
print(arquivo.read())
'''
# seek() -> A função seek() é utilizada para movimentação do cursor pelo arquivo. Ele recebe um
# parâmetro que indica onde queremos colocar o cursor

# Movimentando o cursor pelo arquivo com a função seek() = Procurar
'''
arquivo.seek(0)
print(arquivo.read())

arquivo.seek(21)
print(arquivo.read())
'''

#arquivo = open('leitura_de_arquivo_exemplo.txt')

# readline() -> Função que lê o arquivo linha a linha = lê linha
'''
retorno = arquivo.readline()
print(type(retorno))
print(retorno)
print(retorno.split(' '))
'''

# redlines() -> Função que lê o arquivo linha a linha
# e colocam cada linha sendo um indice em uma lista = lê linhas
'''
# print(arquivo.readlines())
quantidae_de_linhas = arquivo.readlines()
print(len(quantidae_de_linhas))

OBS: Quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo
no disco rigido do computador e o nosso programa. Essa conexão é chamada de streaming. Ao finalizar
os trabalhos como arquivo devemos fechar essa conexão. Para isso utilizamos a função close()
'''

'''
Passos para se trabalhar com arquivos:
'''

# 1 - Abrir o arquivo:
arquivo = open('leitura_de_arquivo_exemplo.txt')

# 2 - Trabalhar o arquivo:
print(arquivo.read())

print(arquivo.closed)  # False - Verifica se o arquivo está aberto ou fechado

# 3 - Fechar o arquivo:
arquivo.close()

print(arquivo.closed)  # True - Verifica se o arquivo está aberto ou fechado

# OBS: Se tentarmos manipular o arquivo após seu fechamento, teremos um ValueError





