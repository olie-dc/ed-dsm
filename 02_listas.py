"""
LISTA é uma estrutura de dados nativa da linguagem Python.
Ela permite que vários valores sejam associados a uma
única variável.
"""

# Lista de strings
frutas = ["maçã", "morango", "laranja", "uva", "manga", "goiaba"]

# Lista de números
nums = [3, 10, -7, 12.8, -0.5, 4, 22]

# Lista com valores de vários tipos (pouco comum)
mistureba = ["Joaquim", 37, 1.81, 79, True]

#### OPERAÇÕES SOBRE LISTAS

# 1) PERCURSO
# Percorrer uma lista significa visitar cada um dos seus
# itens e fazer algo com ele. No exemplo a seguir, vamos
# dar print() em cada uma das frutas da lista
for f in frutas:
    print(f)

# Traço separador
print("-" * 80)

# Percorrendo a lista de números e exibindo o próprio
# número e seu valor elevado a 2
for num in nums:
    print(f"{num} => {num ** 2}")

print("-" * 80)

# 2) INSERÇÃO DE UM NOVO ELEMENTO NO *FIM* DA LISTA: append()
print("frutas, ANTES:", frutas)
print("nums, ANTES:", nums)

# Inserindo novos itens ao final das listas
frutas.append("maracujá")
nums.append(19)

print("frutas, DEPOIS:", frutas)
print("nums, DEPOIS:", nums)

print("-" * 80)

# 3) INSERÇÃO DE UM NOVO ELEMENTO NA POSIÇÃO ESPECIFICADA: insert()
#    Parâmetros:
#    1º ~> a posição onde será feita a inserção (A CONTAGEM COMEÇA
#          EM ZERO!)
#    2º ~> o novo elemento a ser inserido

# Inserindo um novo elemento na PRIMEIRA posição
frutas.insert(0, "melancia")

print("Após inserir melancia na posição 0:", frutas)

# Inserindo um novo elemento na QUARTA posição
frutas.insert(3, "amora")

print("Após inserir amora na posição 3:", frutas)

print("-" * 80)

# 4) Acessando valores, informando a respectiva posição

print("Elemento da QUINTA posição:", frutas[4])
print("Elemento da PRIMEIRA posição", frutas[0])
print("Elemento da ULTIMA posição:", frutas[-1])
print("Elemento da PENULTIMA posição:", frutas[-2])

print("-" * 80)

# 5) Substituindo valores existente

print("ANTES:", frutas)


#Substituindo o valor da posição 3 (QUARTA posição)
frutas[3] = "framboesa"
#Substituindo valore da posição 0 (Primeira posição)
frutas[0] = "pitanga"
#Substituindo valor da posição -1 (Ultima posição)
frutas[-1] = "melão"

print("Depois:", frutas)

# 6) Determinando a quantidade de elementos da lista: len()

print("Quantidade de elementos da lista de frutas:", len(frutas))
print("Quantidade de elementos da lista de números:", len(nums))

print("-" * 80)

# 7) Removendo o *ULTIMO* elemento de uma lista: pop()  (Sem parametros)

print("ANTES:", frutas)
removido = frutas.pop()

print("Valor removido:", removido)
print("Depois:", frutas)

print("-" * 80)

# 8) Removendo um elemento por sua posição: pop() (Com parametros)

print("Removendo elemento da posição 3...")
removido = frutas.pop(3)

print("frutas")

print("-" * 80)


# 9) Removendo um elemento por seu valor: remove()

print("Removendo 'uva'...")
frutas.remove("UVA")
print(frutas)

# 10) Aumentando uma lista com elementos de outra lista: extend()

mais_frutas = ['carambola', 'pera', 'acerola', 'jabuticaba', 'caqui']
frutas.extend(mais_frutas)
print("Adcionando mais frutas a lista...")
print(frutas)

# 11)Fatiando uma lista

#Fatiar significa copiar um pedaço de uma lista (sublista), criando uma nova lista

#Criar uma nova lista com elementos das posições de 2 a 5 (posição 6 *NÃO ENTRA*) da lista de frutas
sublista2a5 = frutas[2:6]
print("Sublista com as frutas das posições de 2 a 5:")
print(sublista2a5)

#Criar uma sublista que contem os elementos desde o inicio ate a posição 6 (posição 7 *NÃO ENTRA*)
sublista_ate6 = frutas[:7]
print("Sublista do inicio ate a posição 6:")
print(sublista_ate6)


#Criar uma sublista que contem os elementos desde a posição 5 ate o final 

sublista_desde5 = frutas[5:]
print("Sublista da posição 5 ate o final:")
print(sublista_desde5)


