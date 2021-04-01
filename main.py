from random import sample, shuffle

class Jugador:
    def __init__(self, name):
        self.nombre = name
        self.puntos = 0



class Juego:
    def __init__(self, jugadores):
        shuffle(jugadores)
        self.jugadores = jugadores
        self.personas = len(jugadores)
        assert 2<personas<9

        self.cartas_oro = [(i, "oro") for i in range(1, 13)]
        self.cartas_espada = [(i, "espada") for i in range(1, 13)]
        self.cartas_copa = [(i, "copa") for i in range(1, 13)]
        self.cartas_basto = [(i, "basto") for i in range(1, 13)]
        self.cartas_comodines = [[0, "comodin"], [0, "comodin"]]

        #unInitialized
        self.mazo = ()
        self.cartas_sin_triunfo = 0
        self.lista_rondas = []
        self._ajustarMazo()

    def jugarRonda(r, m):
        

    def _ajustarMazo(self):
        eliminar_cartas = {
            3:[8,9],    #42
            4:[0],      #48
            5:[],       #50
            6:[0],      #48
            7:[8,9],    #42
            8:[0],      #48
        }
        for n in eliminar_cartas[self.personas]:
            if n==0:
                self.cartas_comodines = []
            else:
                self.cartas_oro.pop(n-1)
                self.cartas_espada.pop(n-1)
                self.cartas_copa.pop(n-1)
                self.cartas_basto.pop(n-1)

        self.mazo = (self.cartas_oro + self.cartas_espada + self.cartas_copa + self.cartas_basto + self.cartas_comodines)
        self.cartas_sin_triunfo = len(self.mazo)s//self.personas
        self.lista_rondas = list(range(1,self.cartas_sin_triunfo,1)) + [self.cartas_sin_triunfo for _ in range(self.personas-1)] + list(range(self.cartas_sin_triunfo,0,-1))


juego = Juego(3)
print(juego.cards)
print(juego.cartas_sin_triunfo)
print(juego.mazo)
print(juego.lista_rondas)
print(juego.rounds)
