"""
range() é uma função da linguagem python que gera uma sequencia (faixa) de numeros. É muito usada em associação
a listas e a instrução for.
"""

# range() com *UM* parametro
# Gera uma sequencia numerica que vai de 0 ate o valor do parametro -1

for num in range(10):
    print(num)

print("-" * 80)

# 2) range() com *DOIS* parametros 
# 1º parametro: valor inicial da sequencia
# 2º parametro: valor final da sequencia (*NÃO INCLUIDO*)

for x in range(10, 17):
    print(x)

print("-" * 80)

# 3) range() com *três* parametros
# 1º parametro: valor inicial
# 2º parametro: valor final(*NÃO INCLUIDO*)
# 3º parametro: valor do passo (intervalo entre um numero e o seguinte)

for n in range(0, 22, 3):
    print(n)

print("-" * 80)

# range() com passo negativo (contagem regressiva)

for i in range(10, 0, -1):
    print(i)



