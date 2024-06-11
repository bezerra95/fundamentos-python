"""
Os decoradores em Python são uma forma de modificar a funcionalidade de uma função ou método existente,
sem a necessidade de alterar seu código original. Eles são representados
pelo símbolo @ seguido do nome do decorador.

No caso dos getters e setters, podemos usar os decoradores @property e @nome_atributo.
setter para criar métodos que se comportam como getters e setters, respectivamente.

Aqui está um exemplo de como usar decoradores para implementar getters e setters em Python:


Neste exemplo, os decoradores @property são usados para criar métodos que se comportam
como getters (nome e idade). Os decoradores @nome.setter e @idade.setter são usados
para criar métodos que se comportam como setters, permitindo a atribuição de novos valores
aos atributos _nome e _idade, respectivamente.
"""
class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, nova_idade):
        if nova_idade >= 0:
            self._idade = nova_idade
        else:
            raise ValueError("A idade deve ser um valor positivo.")

# Exemplo de uso
pessoa = Pessoa("João", 25)

# Obtendo o nome usando o getter
print("Nome:", pessoa.nome)  # Saída: Nome: João

# Definindo um novo nome usando o setter
pessoa.nome = "Maria"

# Obtendo o novo nome usando o getter
print("Novo nome:", pessoa.nome)  # Saída: Novo nome: Maria

# Definindo uma idade inválida usando o setter (irá gerar um erro)
try:
    pessoa.idade = -10
except ValueError as e:
    print("Erro:", str(e))  # Saída: Erro: A idade deve ser um valor positivo.

# Definindo uma idade válida usando o setter
pessoa.idade = 30

# Obtendo a nova idade usando o getter
print("Nova idade:", pessoa.idade)  # Saída: Nova idade: 30
