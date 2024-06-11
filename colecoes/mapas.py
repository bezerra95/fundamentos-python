"""
Mapas -> Conhecidos em Python como Dicionários

Dicionários em Python são representados por chaves ativas {}
"""

#Interar sobre dicionários
'''
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')
'''
#Acessando as chaves
'''
for chave in receita.keys():
    print(receita[chave])
    
print(receita.keys())
'''
#Acessando os valores
'''
for valor in receita.values():
    print(valor)

print(receita.values())
'''
#Desempacotamento de dicionários
'''
for chave, valor in receita.items():
    print(f'chave = {chave} e valor = {valor}')

print(receita.items())
'''

receita = {'jan': 100, 'fev': 250, 'mar': 400}

#Soma*, Valor Máximo*, Valor Mínimo*, Tamanho

# * Se os valores forem todos inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))


