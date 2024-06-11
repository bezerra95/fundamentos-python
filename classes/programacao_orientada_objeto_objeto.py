"""
POO - Objetos

Objetos -> São Instâncias da classe, Ou seja, após o mapeamento do mundo real para sua
representação computacional, devemos poder criar quantos objetos forem necessários. Podemos pensar
nos objetos/instâncias de uma classe como váriaveis do tipo definido na classe.
"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.___cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


#  Instâncias/Objetos
lamp1 = Lampada('Branca', 110, 60)

lamp1.ligar_desligar()

print(f'A Lâmpada está ligada? {lamp1.checa_lampada()}')

cc1 = ContaCorrente(5_000, 20_000)

user1 = Usuario('Julio', 'Cesar', 'jcbs@gmail.com', '123456')

