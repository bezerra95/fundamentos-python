import dunder_primeiro

def funcao2():
    dunder_primeiro.funcao1()


if __name__ == '__main__':
    funcao2()
    print('dunder_segundo.py está sendo executado diretamente.')
else:
    print(f'dunder_segundo.py foi importado. {__name__}')