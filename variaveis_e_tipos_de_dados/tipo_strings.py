"""
Tipo string

Em Python um dado é considerado do tipo string sempre que:
- Estiver entre áspas simple -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre áspas duplas -> "uma string", "234", "a", "True", "42.3"
- Estiver entre áspas simple triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''

nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Gina´s Bar"
print(nome)
print(type(nome))

nome = "Angelina \ " Jolie"
print(nome)
print(type(nome))

print(nome.upper()) # Transforma todas as letra em maiusculas

print(nome.lower()) # Transforma todas as letra em minusculas

print(nome.split()) # Transforma em uma lista de strings
"""
#Estiver entre áspas duplas triplas -> """uma string""" , """234""", """a""", """True""", """42.3"""

# [ 0,    1,   2,   3,   4,   5,   6,   7,   8,   9,    10,   11,   12,   13,   14]
# ['G', 'e', 'e', 'k', ' '  'U', 'n', 'i', 'v', 'e',  'r',  's',  'i',  't',  'y']
nome = 'Geek University'
print(nome[0:4])   # Slice de string
print(nome[4:15])  # Slice de string

# [ 0,      1]
# ['Geek', 'University]
print(nome.split())
print(nome.split()[0])
print(nome.split()[1])
'''
[::-1] -> Comece do preimeiro elemento, vá até o ultimo elemento e inverta
'''
print(nome[::-1])

print(nome.replace('e', 'i')) # Substituir letra da string