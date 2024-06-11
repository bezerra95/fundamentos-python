"""
Escrevendo em arquivos

# OBS: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele. Apenas ler.
De mesma forma, se abrirmos um arquivo para escrita, não podemos lé-lo, somente escrever nele.

# OBS: Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional

Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos a função write().
Esta função recebe uma string como parâmetro, caso contrário um TypeError.

Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existr será criado,
caso ele já exista, o anterior será apagado e um novo será criado. Dessa forma. todo
o conteúdo arquivo anteriro é perdido.
"""


# Exemplo de escrita - modo 'w' - write (escrita)
# Forma Tradicional de escrita em arquivo (Não Pythônica)
'''
arquivo = open('mais.txt', 'w')
arquivo.write('Um texto qualquer\n')
arquivo.write('Mais um texto')
arquivo.close()
'''

# Forma Pythônica
'''
with open('novo.txt', 'w') as arquivo:
    arquivo.write('Escrever dados em arquivo é muito fácil.\n')
    arquivo.write('Podemos colocar quintas linhas quisermos.\n')
    arquivo.write('Esta é a ultima linha.')
'''

with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair:')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break



