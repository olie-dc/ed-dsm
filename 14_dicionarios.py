"""
DICIONÁRIO é uma estrutura de dados nativa da lingagem Python
capaz de armazenar múltiplos valores em uma única variável,
por meio de pares chave-valor (key-value).
Um dicionário é delimitado por chaves {}. Diferentemente da
lista, que tem posições numeradas, o dicionário possui
posições NOMEADAS. Cada uma das posições nomeadas de um
dicionário (ou seja, cada par chave-valor) é chamada de 
PROPRIEDADE.
"""
# Um dicionário com os dados que representam uma pessoa
pessoa = {
    # "chave": valor
    "nome": "Orozimbo Oliveira Osório",
    "sexo": "M",
    "idade": 72,
    "peso": 76,
    "altura": 1.77,
    "aposentado": True,
    "filhos": ["Zeferina", "Adamastor", "Gercina"]
}

# Acessando o valor das propriedades
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Aposentado?", pessoa["aposentado"])

print('-' * 80)  # Traço separador

# Calculando o IMC (Índice de Massa Corporal)
imc = pessoa["peso"] / pessoa["altura"] ** 2

# Nas f-strings delimitadas por aspas duplas, é necessário
# usar aspas simples nos nomes das propriedades (e vice-versa)
print(f"O IMC de {pessoa['nome']} é {imc}.")

############################################################################

# Usando dicionários para representar formas geométricas

forma1 = {
    "base": 7.5,
    "altura": 12,
    "tipo": "R"     # Retângulo
}

forma2 = {
    "base": 6,
    "altura": 3,
    "tipo": "T"     # Triângulo
}

forma3 = {
    "base": 5,
    "altura": 3,
    "tipo": "E"     # Elipse/círculo
}

forma4 = {
    "legume": 10,
    "fruta": 6.2,
    "tipo": "T"
}

forma5 = {
    "base": "batata",
    "altura": False,
    "tipo": "E"
}

from math import pi

def calc_area(forma):
    """
    Função que calcula a área de uma forma geométrica, dados a base,
    a altura e o tipo, passados como propriedades de um dicionário
    """
    match forma["tipo"]:
        case "R":       # Retângulo
            return forma["base"] * forma["altura"]
        case "T":       # Triângulo
            return forma["base"] * forma["altura"] / 2
        case "E":       # Elipse/círculo
            return (forma["base"] / 2) * (forma["altura"] / 2) * pi
        case _:         # Forma inválida
            return None
        
# Testes com a função calc_area()

# formas = [forma1, forma2, forma3, forma4, forma5]
formas = [forma1, forma2, forma3, forma5]

for forma in formas:
    print(f"base: {forma['base']}; altura: {forma['altura']}; tipo: {forma['tipo']}; área: {calc_area(forma)}")