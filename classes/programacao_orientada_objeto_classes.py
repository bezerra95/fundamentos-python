'''
Em POO, Classes nada mais são doque modelos dos objetos do mundo real sendo representados
computacionalmente

Imagine que vc queria fazer um sistema para automatizar o controle das lâmpadas da sua casa.

Classes podem conter:
    - Atributos -> Representam as caracterisiticas do objeto, Ou seja, pelos atributos conseguimos
    representar computacionalmente os estados de um objeto. No caso da lâmpada, possivelmente
    iremos querer saber se a lâmpada é 127V ou 220V volts, se ela é branca, amarela, vermelha ou
    outra cor, qual é a luminosidade dela, etc.

    - Métodos (funções) -> Representam os comportamentos do objeto, Ou seja, as ações que este
    objeto pode realizar no seu sistema. No caso da lâmpada, por exemplo, um comportamento comum
    que muito provavelmente iremos querer representar no nosso sistema é o de ligar e desligar
    a mesma.

Em Python, para definir uma classe, utilizamos a palavra reservada class.

OBS: Utilizamos a palavra "pass" em Python quando temos um bloco de código que ainda não
está implementado.

OBS: Quando nomeamos nossas classes em Python utilizamos por convenção o nome com inicial
Maiúscilo. Se o nome for composto, utiliza-se as inicias de ambas as palvras em
maiúsculo, todas juntas.

Dica Geek: Em computação NÃO utilizamos, Acentuação, caracteres especiais, espaços ou similares
para nomes de Classes, atributos, métodos, arquivos, diretórios, etc.

OBS: Quando estamos planejando um software e definimos quais classes teremos que ter no sistema chamamos
estes objetos que serão mapeados para Classes de entidades.

'''


class Lampada:
    pass


class ContaCorrente:
    pass


class Produto:
    pass


class Usuario:
    pass


class Int:
    pass


valor = int('42')  # cast

print(help(int))

inteiro = Int()

