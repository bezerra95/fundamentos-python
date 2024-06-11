
def funcao1():
    print('Geek University - primeiro.py')


if __name__ == '__main__':
    funcao1()
    print('dunder_primeiro.py está sendo executado diretamente')
else:
    print(f'dunder_primeiro.py foi importado. {__name__}')

