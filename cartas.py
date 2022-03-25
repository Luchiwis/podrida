import random
# class Mazo:
#     def __init__(self):
#         self.cartas = [Carta(palo, numero) for numero in range(1, 13) for palo in ["basto","copa","espada","oro"]]
#         self.barajar()
#     def barajar(self):
#         random.shuffle(self.cartas)
#     def repartir(self):
#         return self.cartas.pop()
#     def __str__(self):
#         return str(self.cartas)

class Carta:
    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor
    def __str__(self):
        return str(self.valor) + self.palo
    def __repr__(self):
        return self.__str__()

        