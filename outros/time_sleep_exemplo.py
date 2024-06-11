from time import sleep

def contador(i, f, p):
    print(f'Contagem de {i} até {f} em {p} e {p}')
    if i < f:
        v = i
        while v <= f:
            print(v, end=' ')
            sleep(0.5)
            v += p
        print()
    else:
        v = i
        while v >= f:
            print(v, end=' ')
            sleep(0.5)
            v -= p
        print()


contador(10, 1, 1)
contador(20, 0, 2)
contador(1, 100, 4)





