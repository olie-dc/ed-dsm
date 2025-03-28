"""
Classe é uma estrutura que representa conjuntamente dados
e algoritmos. Uma classe pode ser comparada a uma "assadeira",
com a qual se pode produzir diferentes tipos de iguarias
assadas, variando os "ingredientes" (dados) da receita e o
"modo de fazer" (algoritmos). Apesar dessas variações, todos
os objetos criados a partir de uma mesma classe terão sempre
algumas características comuns, impressas por ela.
"""
from math import pi

class FormaGeometrica:
    """
    Por convenção, nomes de classes em Python seguem o formato
    PascalCase (primeira letra de cada palavra em maiúsculo).
    Uma classe pode ter, dentro de si, tanto dados quanto funções
    (estas, representando os algoritmos). Uma função especial,
    chamada __init__, é chamada sempre que se tenta criar um novo
    objeto a partir da classe. Essa função especial é chamada
    CONSTRUTOR.
    No contexto de classes e programação orientada a objetos:
    ~> funções passam a ser chamadas MÉTODOS; seu primeiro parâmetro
    é sempre self, que representa o próprio objeto
    ~> variáveis passam a ser chamadas ATRIBUTOS
    """

    def __init__(self, base, altura, tipo):
        """ Método construtor """
        self.base = base
        self.altura = altura
        self.tipo = tipo
        print('Foi executado o método construtor')

    def calc_area(self):
        match self.tipo:
            case "R":
                return self.base * self.altura
            case "T":
                return self.base * self.altura / 2
            case "E":
                return (self.base / 2) * (self.altura / 2) * pi
            case _:
                return None

########################################################################

forma1 = FormaGeometrica(15, 25, "R")
area = forma1.calc_area()

print(f"base: {forma1.base}; altura: {forma1.altura}; tipo: {forma1.tipo}; área: {area}")

forma2 = FormaGeometrica("batata", "cebola", "E")
print(f"base: {forma2.base}; altura: {forma2.altura}; tipo: {forma2.tipo}")
print(f"área de forma2: {forma2.calc_area()}")