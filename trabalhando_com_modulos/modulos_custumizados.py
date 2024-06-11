"""
Módulos Custumizados

Como módulos Python nada mais são do que arquivos Python, então TODOS os arquivos que criamos
neste curso são módulos Python prontos para serem utilizados.
"""

# importando uma função específica do nosso módulo
#from funcoes_com_parametro_padrao import soma_impares
"""
print(soma_impares([1 , 2, 3, 4, 5, 6, 7, 8, 9])
"""

# importando todo o módulo (Temos acesso a todos os Elementos do módulo )
import funcao_com_parametro as fcp

# Estamos acessando e imprimindo uma variavél contida no módulo
"""
print(fcp.lista)

print(fcp.tupla)

print(fcp.soma_impares(fcp.lista))
"""

from map import cidades, c_para_f
print(list(map(c_para_f, cidades)))
