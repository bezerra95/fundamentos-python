"""
POO - Métodos
- Métodos (funções) - > Representam os comportamentos do objeto, Ou seja, as ações
que este objeto pode realizar no seu sistema.

Em python, dividimos os métodos em 2 arquivos:
- Métodos de instância
- Métodos de Classe

Métodos são escritos em letras minúsculas. Se o nome for completo, o nome terá as palavras separadas por underline.
"""

# O método dunder init(__init__) é um método especial chamado construtor e
# sua função é construir o objeto a partir da classe.

# OBS: Todo o elemento em Python que inicia e finaliza com duplo underline é chamado de dunder (Double Underline)
# OBS: Os métodos/funções dunder em Python são chamados de métodos mágicos.


# Métodos de Instância:

class Produto:

    contador = 1

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    # metódo de instância
    def desconto(self, porcentagem):
        """Retorna o valor do produto com o desconto"""
        return (self.__valor * (100 - porcentagem)) / 100


p1 = Produto('Playstation 5', 'Video Game', 3500)  # criando produto objeto
print(p1.desconto(50))  # chamando o método pela instância.
print()

from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:

    # Método construtor
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=2000000, salt_size=16)

    # Método de Instância
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        """Retorna TRUE se a senha for igual ou FALSE se não"""
        if cryp.verify(senha, self.__senha):
            return True
        return False

'''
user1 = Usuario('Julio', 'Cesar', 'jcbs3095@gmai.com', '123456')   # Criando o objeto
user2 = Usuario('Abigail', 'Bezerra', 'abigail%gmail.com', '654321')  # Criando o objeto
print(user1.nome_completo())
print(user2.nome_completo())
'''
nome = input('Informe o nome:  ')
sobrenome = input('Informe o sobrenome:  ')
email = input('Informe o e-mail:  ')
senha = input('Informe a senha:  ')
confirma_senha = input('Confirme a senha:  ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere...')
    exit(1)

print('Usuario criado com sucesso!')

senha = input('Informe a senha para acesso:  ')
if user.checa_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso negado!')

print(f'Senha User Criptografada: {user._Usuario__senha}')  # Acesso errado
print()


# Método de Classe
# Métodos de Classe em Python são conhecidos como Métodos Estáticos em outras Linguagens.

class ContaCorrente:

    contador = 499

    # Método de Classe
    @classmethod
    def conta_cliente(cls):
        print(f'Classe: {cls}')
        print(f'Temos {cls.contador} usuários no sistema')

    # Método estático
    @staticmethod
    def definicao():
        return 'UXR344'

    def ver(self):
        print('teste')

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


cliente_conta_corrente = ContaCorrente(3500, 2600)
ContaCorrente.conta_cliente()  # Forma correta de acessar método de classe
print(ContaCorrente.definicao())