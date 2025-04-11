"""
Programa simples que inverte uma palavra informada pelo usuario e verifica se ela é um PALINDROMO, isto é, 
uma palavra que pode ser lida de trás para frente. Para isso, usaremos uma estrutura de dados pilha baseda
em uma lista nativa da linguagem PYTHON. 
"""

palavra = input('Informe a palavra a ser verificada: ')

#lista vazia que será usada como pilha 
pilha = []

#Parte 1: PREENCHIMENTO DA PILHA
#Pega cada letra da palavra (convertida em maiusculas, para facilitar a posterior comparação) e insere no final (topo) da pilha

for letra in palavra.upper():
    pilha.append(letra)
    print(pilha)
    
print("-" * 80)

#PARTE 2: ESVAZIAMENTO DA PILHA
#Enquanto a pilha nao estiver vazia, vamos retirando a ultima letra dela e concatenando-a à variável inverso

inverso = ""

while len(pilha) > 0:
    letra = pilha.pop()
    inverso += letra
    print(f"PILHA: {pilha}, inverso: {inverso}")

if palavra.upper() == inverso:
    print(f"*** A palavra {inverso} é um PALÍNDROMO ***")
else:
    print(f"--- A palavra {palavra.upper()} NÃO É um palíndromo ---")