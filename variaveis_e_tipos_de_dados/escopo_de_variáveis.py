"""
escopo de variáveis:

dois casos de escopo:

1 - variáveis globais:
    - varáveis globais são reconhecidas, ou seja , seu escopo compreende todo o programa.

2 - variáveis locais:
    - variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    está limitado ao bloco onde foi declarada.

Para declara variáveis em Python fazemos:
nome_da_variável = valor_da_variável
------------------------------------------------------------------------------------------------------------

Python é uma linguagem de tipagem dinâmica. Isso signifca que ao
declararmos uma variável, nos não colocamos o tipo dela.
Este tipo é enferido quando atribuimos um valor á mesma.

"""

numero = 42  # Exemplo de variável global
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))

nao_existo = 'Oi'
print(nao_existo)
print(type(nao_existo))

numero = 42

#Isto é um bloco (função if...)
if numero > 10:
    novo = numero + 10  # Exemplo de variável local (está localizada dentro de um bloco).
    print(novo)


