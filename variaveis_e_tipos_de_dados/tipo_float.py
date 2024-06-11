"""
Tipo Float
Tipo real, decimal
Casa decimais
OBS: Os separados de casa decimais na progrmação é o ponto e não a vírgula.
"""
valor = 1.44
print(valor)
print(type(valor))

# É possivel fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um float para um int
"""
OBS: Ao converter valores float para inteiros, nós perdemos precisão.
"""
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com numeros complexos
variavel = 5j
print(variavel)
print(type(variavel))
