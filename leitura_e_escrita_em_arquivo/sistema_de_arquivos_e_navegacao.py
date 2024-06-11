"""
Sistema de Arquivos e Navegação

Para fazer uso de manipulação de arquivos operacional, precisamos importar
e fazer uso do módulo os.

os -> Operating System - Sistema operacional

"""

# Fazer o import
import os

# getcwd() -> pega o current work directory - diretório de trabalho corrente
# Retorna o path (caminho) absoluto
"""
print(os.getcwd())  # Windows - C:\\Users\\Julio Cesar Bezerra\\PycharmProjects\\_Guppe_AulaPyhon
                    # Linux - /home/Julio Cesar Bezerra/PycharmProjects/_Guppe_AulaPyhon
"""

# Para mudar o diretório, podemos utilizar o chdir()
"""
os.chdir('..')
print(os.getcwd())  # Windows - C:\\Users\\Julio Cesar Bezerra\\PycharmProjects
                    # Linux - /home/Julio Cesar Bezerra/PycharmProjects

os.chdir('..')
print(os.getcwd())  # Windows - C:\\Users\\Julio Cesar Bezerra
                    # Linux - /home/Julio Cesar Bezerra

os.chdir('..')
print(os.getcwd())  # Windwos - C:\\Users
                    # Linux - /home
"""

# Podemos checar se um diretório é absoluto ou relativo
"""
print(os.path.isabs('C:\\Users\\Julio Cesar Bezerra\\')) # True  ->  é absoluto
"""

# Podemos identificar o sistema operacional com o módulo os e sys
"""
print(os.name)  # posix(Linux e Mac),  nt(Windows)
"""

# Podemos ter mais detalhes no sistema operacional
"""
#print(os.uname()) # Linux
import sys
print(sys.platform) # Windows
"""

# Veja que os.path.join() recebe dois parâmetros, sendo o primeiro o diretório atual e o segundo o
# diretório que será juntado ao atual
"""
print(os.getcwd())  # Windows - C:\\Users\\Julio Cesar Bezerra\\PycharmProjects\\_Guppe_AulaPyhon
                    # Linux - /home/Julio Cesar Bezerra/PycharmProjects/_Guppe_AulaPyhon

res = os.path.join(os.getcwd(), 'pacote_diretorio')
os.chdir(res)
print(os.getcwd())  # Windows - C:\\Users\\Julio Cesar Bezerra\\PycharmProjects\\_Guppe_AulaPyhon\\pacote_diretorio
                    # Linux - /home/Julio Cesar Bezerra/PycharmProjects/_Guppe_AulaPyhon/pacote_diretorio
"""

# Podemos Listar os arquivos e diretórios com listdir()
"""
print(os.listdir())
print(len(os.listdir()))
print(os.listdir('C:\\Users'))
print(len(os.listdir('C:\\Users')))
"""

# Podemos Listar os arquivos e diretórios com mais detalhes com scandir()

scanner = os.scandir()

arquivos = list(os.scandir())

print(arquivos)
print(arquivos[0])

print()

print(arquivos[0].inode())
print(arquivos[0].is_dir())  # É um diretório? False
print(arquivos[0].is_file())  # É um arquivo? True
print(arquivos[0].is_symlink())  # É um link simbólico? False
print(arquivos[0].name)  # Nome do arquivo
print(arquivos[0].path)  # Caminho até o arquivo
print(arquivos[0].stat())  # Estatiísticas...

#  OBS: Quando utilizamos a função scandir() nós precisamos fechá-la, assim quando abrimos um arquivo.