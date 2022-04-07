from unittest import TestCase
from jugador import Jugador

class Testing:
    def __init__(self):
        self.context = []
        self.triunfo = None
        self.jugadores = [Jugador("teti"), Jugador("mario"), Jugador("lucio"), Jugador("pablo")]

    def puntuar(self):  #set jugadores.puntos
        """asigna puntaje a los jugadores"""
        for j in self.jugadores:
            puntos = 0
            manos_ganadas = len(j.manos_ganadas)
            manos_pedidas = j.manos_pedidas
            if manos_pedidas == manos_ganadas:
                puntos +=10
            puntos += manos_ganadas
            j.puntos = puntos


if __name__ == "__main__":
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
    t = Testing()
    t.triunfo = "espada"
    g = t.carta_ganadora(mazo)
    print(g)