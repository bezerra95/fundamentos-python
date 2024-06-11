""""
Decorators com diferentes assinaturas

"""

# Relembrando
'''
def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'


@gritar
def ordenar(principal, acomponhamento):
    return f'Olá, eu gostaria de {principal} acompnahado de {acomponhamento}, por favor.'
'''

# Testando
'''
print(saudacao('Julio Cesar'))
print(ordenar('Picanha', 'Batata frita')) # TypeError: aumentar() takes 1 positional argument but 2 were given
'''

#( TypeError: ) - Como resolver, utilizamos um padrão de projeto chamado Decoretor Pattern.

# A assinatura de uma função é representada pelo seu retorno, nome e parâmetros de entrada.

# Refatorando com a Decoretor Pattern.

'''
def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'


@gritar
def ordenar(principal, acomponhamento):
    return f'Olá, eu gostaria de {principal} acompnahado de {acomponhamento}, por favor.'

@gritar
def lol():
    return 'lol'


print(saudacao('Julio Cesar'))
print(ordenar('Picanha', 'Batata frita'))
print(lol())

#OBS: Vale lembrar que podemos utilizar parâmetros nomeados
print(ordenar(acomponhamento='Batata frita', principal='Picanha'))
'''

# Decorator com argumenstos


def verificar_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto, o primeiro valor precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verificar_primeiro_argumento('Pizza')
def comida_favorita(*args):
    return args


@verificar_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


# Testando
print(soma_dez(10, 11))  # 21
print(soma_dez(1, 11))   # Valor inccoreto (primeiro argumto tem que ser = 10)
print()
print(comida_favorita('Pizza', 'Coca-cola'))
print(comida_favorita('Lanche', 'Coca-cola'))

