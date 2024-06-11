"""
POO - Atributos

Atributos -> Representam as caracteristicas do objeto, Ou seja, pelos atributos
nós conseguimos representar computacionalmente os estados de um objeto.

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de Instância;
    - Atributos de Classe;
    - Atributos Dinâmicos;


OBS: Em python, por convenção, ficou estabelecido que todo atributo de uma classe é publico.
Ou seja, pode ser acessado em todo o projeto.

Caso queiramos demosntrar que determinado atributo deve ser tratado como privado, ou seja,
que deve ser acessado/utilizado somente dentro da prórpia classe onde está declarado,
utiliza-se __ duplo underscore no inicio de seu nome.

Isso é conhecido também como Name MangLing.

"""
# Atributos de Instância: São atributos declarados dentro do método construtor.

# OBS: Método construtor: É um método especial utilizado para a construção do objeto.


class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class Usuario:

    def __int__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Atributos PUBLICOS e PRIVADOS


class Acesso:

    def __init__(self, email, senha):
        self.email = email    # PUBLICO
        self.__senha = senha  # PRIVADO

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)

# OBS: Lembre-se que isso é apenas uma convenção, Ou seja, a Linguagem Python não
# vai impedir que façamos acesso aos atributos sinalizados como privados fora da Classe.

# Exemplo
'''
user = Acesso('user@gmail.com', '12345')
print(user.email)
# print(user.__senha)  # AtributeError
print(user._Acesso__senha)  # Temos acesso, mas não deveriamos fazer esse acesso. = Name MangLing

user.mostra_senha()
print()
# O que significa atributos de instância?
'''
# Significa que ao criarmos  instâncias/objetos de uma classe, todas as instâncias
# terão esses atributos.

user1 = Acesso('user1@gmail.com', '12345')
user2 = Acesso('user2@yahoo.com.br', '54321')
user1.mostra_email()
user2.mostra_email()


# Atributos de Classe

# Atributos de classes, são atribuidos, claro, que são declarados diretamente na classe, Ou seja,
# fora do construtor, geralmente já inicializamos um valor, e este valor é compartilhado entre
# todas as instâncias da classe, Ou seja, ao invés de cada instância da classe ter seus própios
# valores como é o caso dos atributos de instância, com os atributos de classe todas as instâncias
# terão o mesmo valor para este atributo.

# Refatorar a classe Produto

class Produto:

    # Atributos de classe
    imposto = 1.05  # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = valor * Produto.imposto
        Produto.contador = self.id


p1 = Produto('Playstation 5', 'Video Game', 3000)
p2 = Produto('XBOX', 'Video Game', 2800)
print(p1.valor)
print(p2.valor)

# OBS: Não precisamos criar uma instância de uma Classe para fazer acesso a um atributo de Classe
print(Produto.imposto)  # Acesso correto de um atributo de classe

print(p1.id)
print(p2.id)

# OBS: Em liguagens Java, os atributos conhecidos como atributos de classe, aqui em Python
# são chamados de atributos estáticos;


class ContaCorrente:

    def __init__(self, nome, limite, senha):
        self.nome = nome
        self.limite = limite
        self.senha = senha


# Atributos Dinâmicos -> Um Atributo de instância que pode ser criado em tempo de execução
# OBS: O Atributo dinâmico será exclusivo da instância que o criou

conta1 = ContaCorrente('Julio Cesar', 10_000, '12345')
conta2 = ContaCorrente('Abigail Bezerra', 100_000, '12345')

# Criando um atributo dinâmico em tempo de execusão
conta1.cartao_credito = 'Visa'  # Note que a classe ContaCorrente não tem atributo cartao de credito

print(f'ContaCorrente - Nome: {conta1.nome}  Limite: {conta1.limite}  Senha: {conta1.senha}  Cartão de Crédito: {conta1.cartao_credito}')
#print(f'ContaCorrente - Nome: {conta2.nome}  Limite: {conta2.limite}  Senha: {conta2.senha}  Cartão de Crédito: {conta2.cartao_credito}')

# Deletando atributos

print(conta1.__dict__)
print(conta2.__dict__)

del conta1.cartao_credito

print(conta1.__dict__)
print(conta2.__dict__)