"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas.

Existem basicamente duas diferenças:

1 - As Tuplas são representadas por parenteses ()
2 - As Tuplas são IMUTÁVEIS: Isso significa que ao se criar uma tupla ela não muda. Toda
 operação em uma Tupla gera uma nova Tupla.

"""

# Cuidado 1: As Tuplas são representadas por parenteses (), mas veja:
"""
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))
"""

# Cuidado 2: Tuplas com 1 elemento
"""
tupla3 = (4) # Isso NÃO é uma tupla!
print(tupla3)
print(type(tupla3))

tupla4 = (4,) # Isso é uma tupla!
print(tupla4)
print(type(tupla4))

tupla5 = 4, # Isso é uma tupla!
print(tupla5)
print(type(tupla5))
"""
# Conclusão: Podemos concluir que tuplas são defenidas pela virgula e não pelo uso de parenteses ()
"""
(4) -> NÃO É TUPLA
(4, ) -> É TUPLA
4, -> É TUPLA
"""

# Podemos gerar uma tupla dinamicamente com range(inicio,fim,passo)
"""
tupla = tuple(range(11))
print(tupla)
print(type(tupla))
"""

#Desempacotamento de tupla
"""
tupla = ('Geek University', 'Programação em Python: Essencial')
escola, curso = tupla
print(escola)
print(curso)
"""
#OBS: Gera erro (ValuesError) se colocarmos um número diferente de elementos para desenpacotar.


# Métodos para adição e remoção nas tuplas NÃO EXISTEM, dado o fato das tuplas serem IMUTÁVEIS.

# Soma*, Valor Maxímo*, Valor Minimo* e Tamanho
# * Se os valores forem todos inteiros ou reais
"""
tupla = (1, 2, 3, 4, 5, 6)
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))
"""


# Contatenação de tuplas
"""
tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2)  # Tuplas são imutáveis
print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2
print(tupla3)
print(tupla1)
print(tupla2)

tupla1 = tupla1 + tupla3  # Tuplas são imutáveis, mas podemos sobrescrever seus valores.
"""


# Verificar se determinado elemento está contido na tupla
"""
tupla = (1, 2, 3,)
print(3 in tupla)
"""

# Iterando sobre uma tupla
"""
tupla = (1, 2, 3)
for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)
"""


# Contando elementos dentro de uma (tupla)
"""
tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla.count('c'))

escola = tuple('Geek University')
print(escola)
print(escola.count('e'))
"""


# Dicas na utilização de tuplas
# DEVEMOS USAR TUPLAS SEMPRE QUE NÃO PRICISARMOS MODIFICAR OS DADOS CONTIDOS EM UMA COLEÇÃO

# Exemplo 1
"""
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
         'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(meses)
"""

# O Acesso a elemento de uma tupla é semelhante a de uma lista
"""
print(meses[5]) # = Junho

# Itera com while
i = 0
while i < len(meses):
    print(meses[i])
    i += 1
"""

# Verificamos em qual indice um elemento está na tupla
"""
print(meses.index('Junho'))
# OBS: Caso o elemento não eista, será gerdo ValueError.
"""

# Slicing
# tupla[inicio:fim:passo]
"""
print(meses[5:9])
"""

# OBS: Por quê utilizar tuplas?
# - Tuplas são mais rápidas do que listas.
# - Tuplas deixam seu codigo mais seguro*.
# * Isso porque trabalhar com elementos imutáveis traz segurança para o código.
"""
"""
 # Copiando uma tupla para outra
"""
tupla = (1, 2, 3)
print(tupla)
nova = tupla #Na tupla não temos o problema de Shallow Copy
print(nova)
print(tupla)

outra = (4, 5, 6)
nova = nova + outra
print(nova)
print(tupla)
"""