def fatorial_iter(num):
    """
    Calcula o fatorial de um número usando um algoritmo
    ITERATIVO (não recursivo)
    """
    if num < 0:
        raise Exception("ERRO: número negativo, cálculo impossível")
    resultado = 1
    for n in range(num, 0, -1): resultado *= n
    return resultado

##########################################################

print('O fatorial de 6 é', fatorial_iter(6))

##########################################################

def fatorial_rec(num):
    """
    Cálculo do fatorial, usando um algoritmo RECURSIVO
    """
    if num < 0:
        raise Exception("ERRO: número negativo, cálculo impossível")
    if num <= 1: return 1   # o fatorial de 0 e 1 = 1
    else: return num * fatorial_rec(num - 1)

##########################################################

print('O fatorial de 6 é', fatorial_rec(6))  