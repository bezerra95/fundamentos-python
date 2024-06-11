"""
Estruturas condicionais
if, else, elif
"""
idade = int(input("Qual é sua idade"))

"""
# Estrutura condicional if, em C

if(idade < 18) {
    printf("Menor de idade");
}       
"""
if idade < 18:
    print(f'Menor de idade')
else:
    print('Maior de idade')

    #    OU

if idade >= 16:
    print('Pode vota')
elif idade == 18:
    print('É Maior de idade e pode vota')
else:
    print('Não pode vota')

