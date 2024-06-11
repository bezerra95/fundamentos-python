"""
Geradores

- Geradores (Generators) são Iterators (Iteradores):

OBS: O contrario não é verdadeiro. Ou seja, nem todo iterator é um generator.

Outras informações:
- Generators podem ser criados com funções geradoras:
- Funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com Expressões Geradoras;

Diferença entre funções e Generator Functions (Funções Geradoras)

---------------------------------------------------------------------------------
|  Funções                              |  Generator Functions                  |
---------------------------------------------------------------------------------
|  utilizam return                      |  utilizam yield                       |
---------------------------------------------------------------------------------
|  retorna uma vez                      |  podem utiliza yield múltiplas vezes  |
---------------------------------------------------------------------------------
|  quando executada, retorna um valor   | quando executada, retorna um generator|
---------------------------------------------------------------------------------


"""

# Exemplo Função Geradora (Generator Function)


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

# OBS: Uma Generator Function não é um Generator. Ela gera um generator.


'''
gen = conta_ate(5)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
'''

'''
gen = conta_ate(10)
for numero in gen:
    print(numero)
'''

'''
gen = conta_ate(10)
print(next(gen))  # = 1
print('Geek')
for numero in gen:
    print(numero)
'''

