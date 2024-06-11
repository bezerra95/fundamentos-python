"""
Estrturas Lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
    - not, is
Operadores binários:
    - and, or

Regras de funcionamento:

Para o 'and', ambos os valores tem que ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor do booleano é invertido, ou seja, se for True vira False, se for False vira True
Para o 'is', o valor é comparado com um segundo

"""
ativo = False
logado = True

# Se ativo e logado for VERDADEIRO:
if ativo and logado:
    print('Bem-vindo usuário!')
else:
    print('Você precisa ativar sua conta por favor, cheque seu e-mail')

# ativo é verdadeiro?
print(ativo is True)



