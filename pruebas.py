from pprint import pprint
mazo = [
    (1, "oro"),
    (2, "oro"),
    (3, "oro"),
    (4, "oro"),
    (5, "oro"),
    (6, "oro"),
    (7, "oro"),
    (8, "oro"),
    (9, "oro"),
    (10, "oro"),
    (11, "oro"),
    (12, "oro"),
    (1, "espada"),
    (2, "espada"),
    (3, "espada"),
    (4, "espada"),
    (5, "espada"),
    (6, "espada"),
    (7, "espada"),
    (8, "espada"),
    (9, "espada"),
    (10, "espada"),
    (11, "espada"),
    (12, "espada"),
    (1, "copa"),
    (2, "copa"),
    (3, "copa"),
    (4, "copa"),
    (5, "copa"),
    (6, "copa"),
    (7, "copa"),
    (8, "copa"),
    (9, "copa"),
    (10, "copa"),
    (11, "copa"),
    (12, "copa"),
    (1, "basto"),
    (2, "basto"),
    (3, "basto"),
    (4, "basto"),
    (5, "basto"),
    (6, "basto"),
    (7, "basto"),
    (8, "basto"),
    (9, "basto"),
    (10, "basto"),
    (11, "basto"),
    (12, "basto"),
]

context = []
fallo = False
triunfo = "copa"

def cartas_jugables(cartas):
        """retornar cartas que se pueden jugar de un conjunto de cartas dependiendo del contexto"""
        if not context:
            return cartas
        else:
            mano_actual = max(list(filter(lambda carta :carta[1] == context[0][1], context))) #carta mas alta del mismo palo de la primera carta tirada
            ultimo_triunfo_mas_alto = max(list(filter(lambda carta :carta[1] == triunfo, cartas)))  #triunfo mas alto tirado

            cumplen_regla_1 = list(filter(lambda carta :carta[0]>=mano_actual[0] and carta[1] == mano_actual[1], cartas)) #regla1 (mayor del mismo palo)
            cumplen_regla_2 = list(filter(lambda carta :carta[1] == mano_actual[1], cartas)) #regla2   (mismo palo)
            cumplen_regla_3_0 = list(filter(lambda carta :carta[0]>=ultimo_triunfo_mas_alto[0] and carta[1] == triunfo, cartas)) #regla3.0 (hay triunfo mas alto que el anterior)
            cumplen_regla_3_1 = list(filter(lambda carta :carta[1] == triunfo, cartas)) #regla3.1 (hay triunfo)

            if cumplen_regla_1:
                return cumplen_regla_1
            elif cumplen_regla_2:
                return cumplen_regla_2
            elif cumplen_regla_3_0:
                return cumplen_regla_3_0
            elif cumplen_regla_3_1:
                return cumplen_regla_3_1
            else:
                return cartas


for i in range(4):



##TESTINGGGGG