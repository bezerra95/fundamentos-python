"""
Leitura de Arquivos

Para o conteúdo de um arquivo em Python, utilizamos a função integrada open(),
que literalmente significa 'abrir'.

open() -> Na forma mais simples de utilização nós passamos apenas um parâmetro
de entrada, que neste caso é o caminho para o arquivo a ser lido. Essa função retorna
um_io. TextIOWrapper e é com ele que trabalhamos então.

https://doc.python.org/3/library/functíons.html#open

# OBS: Por padrão, a função open() abre o arquivo para leitura. Este arquivo
deve existir, ou então teremos o erro FileNotFoundError

<_io.TextIOWrapper name='leitura_de_arquivo_exemplo.txt' mode='r' encoding='cp1252'>

mode r -> Modo de Leitura. r -> read() -> ler
"""

# Exemplo

arquivo = open('leitura_de_arquivo_exemplo.txt')

# print(arquivo)

# print(type(arquivo))

# Para ler o conteúdo de um arquivo, após sua abertura, devemos utilizar a função read()
print(arquivo.read()) # retorna uma string

# OBS: O Python, utiliza um recurso para trabalhar com arquivos chamado cursor. Esse cursor,
# funciona como o cursor de quandos estamos digitando.

# OBS: A função read() lè todo o conteúdo do arquivo.

# Com a função read() podemos limitar a quantidade de caracteres a serem lidos no arquivo
print(arquivo.read(21))


