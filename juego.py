from ronda import Ronda
from random import shuffle

class Juego:
    """
    Hay un juego, cada juego tiene X cantidad de rondas y cada ronda tiene Y cantidad de manos
    """
    def __init__(self, jugadores):
        self.jugadores = jugadores
        shuffle(self.jugadores)              #determina el orden de los jugadores, 0 es mano en la primera ronda
        self.cantidad_jugadores = len(jugadores)
        assert 3 <= self.cantidad_jugadores <= 8  #la cantidad de jugadores debe estar entre 3 y 8

        #mazo ordenado
        self.cartas_oro = [(i, "oro") for i in range(1, 13)]
        self.cartas_espada = [(i, "espada") for i in range(1, 13)]
        self.cartas_copa = [(i, "copa") for i in range(1, 13)]
        self.cartas_basto = [(i, "basto") for i in range(1, 13)]
        self.cartas_comodines = [[0, "comodin"], [0, "comodin"]]

        # unAssigned vars
        self.mazo = ()                                  #el mazo con las cartas totales con las que se va a desarrollar el juego
        self.cartas_sin_triunfo = 0                     #las rondas sin triunfo se van a jugar con esta cantidad de cartas
        self.lista_rondas = []                          #lista con los numeros de cartas repartidas en cada ronda [1,2,3,4, ... , 4,3,2,1]
        self.lista_pies = []

        # just assigned vars
        self._ajustarMazo()                             #ajusta el mazo, las cartas sin triunfo y la lista de rondas
        self.cantidad_rondas = len(self.lista_rondas)   #int que indica la cantidad de rondas totales




    def jugar(self):
        for r,p in zip(self.lista_rondas,self.lista_pies):
            Ronda(r, p, self.jugadores, self.mazo)

    def _ajustarMazo(self): #set mazo, set cartas_sin_triunfo, set lista_rondas
        "ajusta el mazo en funcion de la cantidad de jugadores"
        eliminar_cartas = {
            3: [8, 9],  # 42
            4: [0],  # 48
            5: [],  # 50
            6: [0],  # 48
            7: [8, 9],  # 42
            8: [0],  # 48
        }
        for n in eliminar_cartas[self.cantidad_jugadores]:
            if n == 0:
                self.cartas_comodines = []
            else:
                self.cartas_oro.pop(n - 1)
                self.cartas_espada.pop(n - 1)
                self.cartas_copa.pop(n - 1)
                self.cartas_basto.pop(n - 1)

        self.mazo = (
            self.cartas_oro
            + self.cartas_espada
            + self.cartas_copa
            + self.cartas_basto
            + self.cartas_comodines
        )

        self.cartas_sin_triunfo = len(self.mazo) // self.cantidad_jugadores

        self.lista_rondas = (
            list(range(1, self.cartas_sin_triunfo, 1))
            + [self.cartas_sin_triunfo for _ in range(self.cantidad_jugadores - 1)]
            + list(range(self.cartas_sin_triunfo, 0, -1))
        )

        #TODO: test
        self.lista_pies = [self.jugadores[i] for i in range(len(self.jugadores)) for _ in range(len(self.lista_rondas)//len(self.jugadores))]

