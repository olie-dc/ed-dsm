"""
Programa simples que verifica o balanceamento de parenteses em expressoes maatematicas usando pilha
"""

from lib.stack import Stack

pilha = Stack()

#Testes com todas as possiveis possibilidades 
#expr = "(2 * (3 + 4) - (5 / 3) + 1) -2"
#expr = "(2 * (3 + 4) - ((5 / 3) + 1) -2"
expr = "(2 * (3 + 4)) - (5 / 3) + 1)) -2"

for pos in range(len(expr)):

    #1º PARTE: Percorre a expressao e EMPILHA as posições onde são encontrados os caracteres de abre parentese
    if expr[pos] == "(": pilha.push(pos)

    #2° PARTE: Ao encontrar um caractere de fecha parentese, tenta desempilhar
    elif expr[pos] == ")":
        #A pilha não pode estar vazia quando for encontrado um fecha parentese
        if pilha.is_empty():
            print(f"ERRO: parentese fechado na posição {pos} não tem o abre correspondente")
        else:
            pos_emp = pilha.pop()
            print(f"Parentese aberto na posição {pos_emp} foi fechado na posição{pos}.")

print(pilha)

# <~ CUIDADO COM A IDENTAÇÃO AQUI 
#Processa eventuais sobras na pilha após o termino da analise da expressao 
while not pilha.is_empty():
    pos_emp =  pilha.pop()
    print(f"ERRO: Parentese aberto na posição {pos_emp} não tem o fecha correspondente")