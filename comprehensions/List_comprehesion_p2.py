"""
List Comprehensíon

Nós podemos adicionar estruturas condicionais lógicas as nossas List Comprehension
"""

# Exemplos

# 1

numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]  # Si numero for par, para cada numero em numeros imprima numero
impares = [numero for numero in numeros if numero % 2 != 0]  # Si numero for impar, para cada numero em numeros imprima numero

print(pares)
print(impares)

# Refatorar

# Qualquer número par módulo de 2 é 0, e 0 em Python é False. not False = True
pares = [numero for numero in numeros if not numero % 2]  # Si numero for par, para cada numero em numeros imprima numero

# Qualquer número ímpar módulo de 2 é 1, e 1 em Python é True
impares = [numero for numero in numeros if numero % 2]  # Si numero for impar, para cada numero em numeros imprima numero

print(pares)
print(impares)


res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]  # Para cada numero em numeros, multiplica pramin, Si o numero for par, Si não dividi pramin
print(res)
