# Variável global para a contagem de comparações
comps = None

def busca_binaria(lista, val):
    """
    ALGORITMO DE BUSCA BINÁRIA
    Dada uma lista, que deve estar PREVIAMENTE ORDENADA, e um valor
    de busca, divide a lista em duas partes, procurando pelo valor
    de busca apenas na parte onde o valor de busca poderia estar.
    Novas subdivisões são feitas até que se encontre o valor de 
    busca ou que reste apenas uma sublista vazia, quando então se
    conclui que o valor de busca não existe na lista.
    """
    global comps    # Avisa que estamos usando uma variável global
    comps = 0

    ini = 0                 # Posição inicial da lista
    fim = len(lista) - 1    # Posição final da lista

    while ini <= fim:
        # Calculando a posição do meio da lista
        meio = (ini + fim) // 2     # Divisão inteira

        # Verifica se o valor que está no meio da lista é igual ao valor
        # de busca. Em caso afirmativo, retornamos a posição do meio,
        # pois o valor de busca foi encontrado
        if val == lista[meio]: 
            comps += 1
            return meio

        # Senão, se o valor de busca é MENOR do que o valor do meio, move
        # o ponteiro do fim para a posição anterior à do meio e reinicia
        # a busca na metade ESQUERDA da (sub)lista
        elif val < lista[meio]: 
            comps += 2
            fim = meio - 1

        # Por fim, se o valor de busca é MAIOR do que o valor do meio da
        # lista, move o ponteiro do início para a posição seguinte à do
        # meio e reinicia a busca na metade direita da (sub)lista
        else: 
            comps += 2
            ini = meio + 1

    # <-- CUIDADO COM A INDENTAÇÃO AQUI!
    # Se chegamos a esse ponto, é porque o valor de busca não existe na
    # lista
    return -1

############################################################################

import sys
sys.dont_write_bytecode = True      # Impede a criação do cache

from time import time

# TESTES COM AS LISTAS DE NOMES
from data.nomes_completos import nomes

buscas = [
    "EDSON PEREIRA",
    "MARIA FERREIRA",
    "VALDIR SILVA",
    "FAUSTO SILVA",
    "GILCINEIA GARCIA"
]

for b in buscas:
    hora_ini = time()
    pos = busca_binaria(nomes, b)
    hora_fim = time()
    if pos >= 0:
        print(f"Nome {b} encontrado na posição {pos}.")
        print(f"Quantidade de comparações: {comps}")
    else:
        print(f"Nome {b} não encontrado na lista.")
        print(f"Quantidade de comparações: {comps}")

    print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms.\n")