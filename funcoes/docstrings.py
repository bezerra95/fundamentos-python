"""
Documentado funções com Docstrings

OBS: Podemos ter acesso á documentação de uma função em python
utilizando o propriedade especial __doc__

Podemos ainda fazer acesso á documetação com a fução help()
"""

# Exemplos

def diz_oi():
    """Uma funcão simples que retorna a string 'Oi'!"""
    return 'Oi!'


def exponencial(numero, potencia=2):
    """
    Funcao que retorna por padrao o quadrado de 'numero' ou 'numero' a 'potencia' informada
    :param numero: Numero que desejamos gerar o exponencial.
    :param potencia: Potencia que queremos gera o exponencial. Por padrao e 2.
    :return: Retorna o exponencial de 'numero' por 'potencia'
    """
    return numero ** potencia