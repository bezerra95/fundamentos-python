"""
Em Python, decoradores são funções que recebem outras funções como argumento e
adicionam funcionalidades a elas, sem modificar o seu código fonte original.
Eles são usados para modificar ou estender o comportamento das funções
 sem que se precise alterá-las diretamente.

Um decorador é definido usando a sintaxe "@" seguida pelo nome da função decoradora.
"""

print('EXEMPLO 1')


# Definição de uma função com decorador
def meu_decorador(funcao):
    def funcao_decorada():
        print("Antes da função")
        funcao()
        print("Depois da função")
    return funcao_decorada


# Função que será decorada
@meu_decorador
def minha_funcao():
    nome = "Maria"
    idade = 25
    print(f"{nome} tem {idade} anos")


# Chamada da função decorada
minha_funcao()


print('\nEXEMPLO2')


# Definição de uma função com decorador
def exibir_nome(funcao):
    def wrapper(n):
        print(f"O nome é: {n}")
        funcao(n)
    return wrapper


# Função que será decorada
@exibir_nome
def saudacao(nome):
    print(f"Olá, {nome}!")


saudacao("João")
