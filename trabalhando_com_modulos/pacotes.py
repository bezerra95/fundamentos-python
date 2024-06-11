"""
Pacotes

Módulo é apenas um arquivo python que pode ter diversas funções para utilizarmos;

Pacote -> É um diretório contendi coleção de módulos;
"""

from pacote_diretorio import modulo_um
print(modulo_um.soma(10, 10))

print()

from pacote_diretorio import modulo_um, modulo_dois
print(modulo_dois.multipica(10, 10))
print(modulo_um.soma(10, 10))

print()

from pacote_diretorio.pacote_diretorio_dois import modulo_tres
print(modulo_tres.dividi(10, 10))

print()

from pacote_diretorio.pacote_diretorio_dois import modulo_tres, modulo_quatro
print(modulo_tres.dividi(10, 10))
print(modulo_quatro.subtrai(10, 10))

print()

from pacote_diretorio.modulo_um import soma
from pacote_diretorio.pacote_diretorio_dois.modulo_quatro import subtrai
print(subtrai(10, 10))
print(soma(10, 10))