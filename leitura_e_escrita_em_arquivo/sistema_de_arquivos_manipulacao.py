"""
Sistema de Arquivos - Manipulação


"""
import os
# Descobrindo se um arquivo ou diretório existe

# Arquivo
'''
print(os.path.exists('arquivo.txt'))  # False
print(os.path.exists('frutas.txt'))  # True
'''
# Diretório
# Paths relativos
'''
print(os.path.exists('pacote_diretorio'))  # True
print(os.path.exists('pacote_diretorio/pacote_diretorio_dois'))  # True
print(os.path.exists('pacote_diretorio/pacote_diretorio_dois/modulo_tres.py'))  # True
print(os.path.exists('outro'))  # False
'''
# Paths absolutos
'''
print(os.path.exists('C:\\Users\\Julio Cesar Bezerra\\Images'))  # False
print(os.path.exists('C:\\Users\\Julio Cesar Bezerra\\PycharmProjects'))  # True
'''

# Criando Diretórios - únicos (um á um)
# Path Relativo
'''
os.mkdir('diretorio-sistema_de_arquivos_manipulacao')
'''
# Path Absoluto
'''
os.mkdir(C:\\Users\\Julio Cesar Bezerra\\Desktop\\university')
'''
# OBS: A Função mkdir() cria um diretório se este não existir. Casa exista, teremos FileExistsError
# OBS: Se não tivermos permissão para criar o dretório teremos um PermissonError

# Criando multi-diretórios (árvore de diretórios)
'''
os.makedirs('exemplo_sistema_de_arqv_mplç/geek/university')
'''
# OBS: Se já existir, teremos um FileExistsError

# Caso exista esse diretorio e pra não haver erros, evitamos da seguinte maneira:
'''
os.makedirs('exemplo_sistema_de_arqv_mplç/geek/university', exist_ok=True)
'''

# Renomeando arquivos e diretórios

# Diretórios
'''
os.rename('exemplo_sistema_de_arqv_mplç', 'exemplo_sistema_de_arqv_mplç.teste')
'''
# OBS: Se o diretório não existir teremos um FileExistsError
# OBS: Se o diretório que queremos renomear não estiver vazio, teremos um OSError

# Arquivos
'''
os.rename('pacote_diretorio/pacote_diretorio_dois/teste.txt', 'pacote_diretorio/pacote_diretorio_dois/geek.txt')
'''
'''
os.rename('frutas.txt', 'cesta_de_frutas.txt')
'''

# Removendo arquivos e diretórios
# ATENÇÃO! Tome cuidado com os comandos de deletação. Ao deletarmos um arquivo ou diretório, eles
# não vão para a lixeira. Eles somem.

# Removendo arquivos
'''
os.remove('pacote_diretorio/pacote_diretorio_dois/geek.txt')
'''
# OBS: Se você estiver no Windows e o arquivo que você for deletar estiver em uso, você terá um erro.
# OBS: Caso o arquivo não exista, teremos o FileNotFoundError
# OBS: Se você informar um diretório ao invés de um arquivo, teremos um IsADirectoryError

# Removendo diretórios vazios
'''
os.rmdir('template')
'''
# OBS: Se o diretório tiver qualquer conteúdo teremos OSrror
# OBS: Se o diretório não existir teremos um FileFoundError

# Removendo árvore de arquivos
'''
for arquivo in os.scandir('geek2'):
    if arquivo.is_file():
        os.remove(arquivo.path)
'''

# Podemos remover uma árvore de diretórios vázios
'''
os.removedirs('geek2/mais')
'''
# Se Algum dos diretórios contiver arquivos ou outros diretórios, o processo para.
# ATENÇÃO! Ao remover arquivos e diretórios com Python eles não vão para a lixeira. Eles vão embora!

# Importando a biblioteca send2trash
'''
from send2trash import send2trash
os.remove('cesta1.txt')  # Não vai para a lixeira. É deletado imediatamente
send2trash('cesta2.txt') # Vai para a lixeira. Pode ser restaurado.
'''
# OBS: Se o arquivo não existir, teremos OSError

# Trabalhando com arquivos e diretórios temporários
import os
import tempfile
'''
with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek University\n')
    input()
'''
# Estamos criando um diretório temporário, abrindo o mesmo e dentro dele criando
# um arquivo para escrevermos um texto. No final, usamos um input() só para mantermos
# os arquivos temporários 'vivos' dentro dos blocos with.

# OBS: possívelmente, o código acima não irá funcionar no windows
# por conta desse sistema trabalhar de forma diferente com arquivos temporários.


# Criando arquivos temporários
import tempfile
with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University\n')
    tmp.seek(0)
    print(tmp.read())


'''
https://docs.python.org/3/library/os.html?highlight=os#module-os
'''