"""
Saindo de loops com break.

Utilizamos o break para sair de loops de maneira projetada.
"""

# Exemplo 1
for numero in range(1, 11):
    if numero == 5:
        break
    else:
        print(numero)
print('Sai do loop')

# Exemplo 2
while True:
    sair = input('Pedi para sair?')
    if sair == 'quero sair':
        break


