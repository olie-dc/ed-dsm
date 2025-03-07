# Variáveis de estatística
comps = trocas = passd = None

def bubble_sort(lista):
    """
    ALGORITMO DE ORDENAÇÃO BUBBLE SORT
    Percorre a lista a ser ordenada em sucessivas passadas, 
    trocando entre si dois elementos adjacentes sempre que
    o segundo for MENOR do que o primeiro. Efetua tantas
    passadas quanto forem necessárias, até que, na última
    passada, nenhuma troca tenha sido efetuada.
    """
    global comps, trocas, passd
    comps = trocas = passd = 0

    # Loop eterno: não sabemos antecipadamente quantas passadas
    # serão necessárias
    while True:

        passd += 1      # Iniciando uma nova passada

        # Variável que controla se houve trocas na passada
        trocou = False

        # Percurso da lista, do primeiro ao PENÚLTIMO elemento,
        # com acesso a cada posição
        for pos in range(len(lista) - 1):
            # Se o valor que está à frente na lista (pos + 1)
            # for MENOR do que aquele que está atrás (pos),
            # efetuamos uma troca entre eles
            comps += 1      # O if abaixo representa uma comparação
            if lista[pos + 1] < lista[pos]:
                lista[pos + 1], lista[pos] = lista[pos], lista[pos + 1]     # Troca
                trocas += 1
                trocou = True

        # <-- CUIDADO COM A INDENTAÇÃO AQUI
        # Se não houve troca na passada (trocou é False), a lista
        # está ordenada e interrompemos o loop eterno while
        if not trocou: break

#######################################################################

# nums = [7, 9, 5, 4, 0, 3, 8, 1, 6, 2]   # Caso médio
# 72 comparações, 30 trocas, 8 passadas

# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]   # Melhor caso
# 9 comparações, 0 trocas, 1 passada

nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]     # Pior caso
# 90 comparações, 45 trocas, 10 passadas

# Para o pior caso, os números de comparações, trocas e passadas
# podems ser calculados da seguinte forma (n = número de elementos no vetor)
# Comparações: (n ** 2) - n
# Trocas: ((n ** 2) - n) / 2
# Passadas: n

print("ANTES: ", nums)
bubble_sort(nums)
print("DEPOIS:", nums)
print(f"Comparações: {comps}; trocas: {trocas}; passadas: {passd}")

#########################################################################

from time import time

import sys
sys.dont_write_bytecode = True      # Impede a criação do cache

# TESTE COM A LISTA DE NOMES
from data.nomes_desord import nomes

# Trabalhando apenas com os primeiros 100k nomes
nomes = nomes[100000:]

hora_ini = time()
bubble_sort(nomes)
hora_fim = time()

print(nomes)

print(f"Comparações: {comps}; trocas: {trocas}; passadas: {passd}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms.\n")