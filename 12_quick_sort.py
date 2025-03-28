# Variáveis de estatística
passd = comps = trocas = None

def quick_sort(lista, ini = 0, fim = None):
    """
    ALGORITMO DE ORDENAÇÃO QUICK SORT
    Escolhe um dos elementos da lista para ser o pivô (na
    nossa implementação, será o último) e, na primeira
    passada, divide a lista, a partir da posição final do
    pivô, em uma sublista à esquerda, contendo apenas
    valores menores que o pivô, e outra sublista à direita,
    contendo apenas valores maiores que o pivô.
    Em seguida, recursivamente, repete o processo em cada
    uma das sublistas, até que toda a lista esteja ordenada.
    """
    global passd, comps, trocas

    passd += 1

    # Quando o valor do parâmetro 'fim' não for passado,
    # atribuímos a ele o valor da última posição da lista
    if fim is None: fim = len(lista) - 1

    # Para que seja possível a ordenação, é necessário que
    # a faixa delimitada pelos parâmetros 'ini' e 'fim'
    # tenha, pelo menos, DOIS elementos. Caso contrário,
    # saímos da função sem fazer nada
    if fim <= ini: return

    # Inicialização das variáveis
    pivot = fim     # Última posição da faixa
    div = ini - 1   # Uma posição antes do início da faixa

    # Percorre a lista da posição 'ini' até a posição 'fim' - 1
    for pos in range(ini, fim):
        # Se o elemento da posição 'pos' for MENOR do que o elemento
        # da posição 'pivot', executa algumas ações
        comps += 1
        if lista[pos] < lista[pivot]:
            div += 1        # Avança 'div' em uma posição
            # Efetua a troca entre os elementos das posições 'pos' e
            # 'div', caso estas sejam diferentes entre si
            if pos != div:
                lista[pos], lista[div] = lista[div], lista[pos]
                trocas += 1

    # <~ CUIDADO COM A INDENTAÇÃO AQUI!
    # Após o loop 'for' anterior terminar, o valor de 'div' ainda
    # avança uma posição
    div += 1

    # Trocamos os elementos das posições 'div' e 'pivot' entre si,
    # caso o último seja MENOR do que o primeori. Com isso, o valor da
    # posição 'pivot' é colocado no seu lugar correto dentro da lista
    # ordenada
    comps += 1
    if lista[pivot] < lista[div]:
        lista[div], lista[pivot] = lista[pivot], lista[div]
        trocas += 1

    # Neste momento, todos os elementos à esquerda do pivô são MENORES
    # do que ele, enquanto todos os elementos à sua direita são MAIORES
    # do que ele. Chamamos a função recursivamente para ordenar as
    # sublistas direita e esquerda
    quick_sort(lista, ini, div - 1)
    quick_sort(lista, div + 1, fim)

###################################################################################  

# Zerando as variáveis de estatística
passd = comps = trocas = 0

# nums = [7, 9, 5, 4, 0, 3, 8, 1, 6, 2]   # Caso médio 
# Comparações: 27; trocas: 8; passadas: 13

# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]   # Melhor caso
# Comparações: 54; trocas: 0; passadas: 19

nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]     # Pior caso

print("ANTES: ", nums)
quick_sort(nums)
print("DEPOIS:", nums)
print(f"Comparações: {comps}; trocas: {trocas}; passadas: {passd}")

#####################################################################

from time import time

import sys, tracemalloc
sys.dont_write_bytecode = True      # Impede a criação do cache

# TESTE COM A LISTA DE NOMES
from data.nomes_desord import nomes

# Trabalhando apenas com os primeiros 100k nomes
# nomes = nomes[100000:]

# Zerando as variáveis de estatística
passd = comps = trocas = 0

tracemalloc.start()     # Inicia a medição do consumo de memória
hora_ini = time()
quick_sort(nomes)
hora_fim = time()

# Captura as informações do consumo de memória
mem_atual, mem_pico = tracemalloc.get_traced_memory()

print(nomes)

print(f"Comparações: {comps}; trocas: {trocas}; passadas: {passd}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms.\n")
print(f"Pico de memória: {mem_pico / 1024 / 1024} MB")