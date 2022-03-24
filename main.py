from random import sample, shuffle


class Jugador:
    def __init__(self, name):
        self.nombre = name
        self.puntos = 0

        #en ronda
        self.cartas = []
        self.cartasJugables = []
        self.manos_ganadas = []
        self.apuesta = None #int


    def turno(self,cartas_jugables):
        pass

    def tirar_carta(self,carta):
        pass


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

        # just assigned vars
        self._ajustarMazo()                             #ajusta el mazo, las cartas sin triunfo y la lista de rondas
        self.cantidad_rondas = len(self.lista_rondas)   #int que indica la cantidad de rondas totales







    # def jugarRonda(self, ronda, mano):
    #     pass

    def _ajustarMazo(self):
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


class Ronda:
    def __init__(self, cartas_por_jugador, jugador_mano, jugadores, mazo):
        self.jugadores = jugadores
        self.jugador_mano = jugador_mano
        self.cartas_por_jugador = cartas_por_jugador
        self.mazo = mazo

        self.triunfo = None
        self.fallo = False
        self.context = []   #historial de cartas jugadas

        self.jugar_mano()
    
    def jugar_mano(self):
        #enviar solicitud al jugador mano

        #enviar solicitud al segundo jugador y esperar

        # ...

        #determinar ganador de la mano

        #sumar mano al ganador

        pass

    #TODO: TESTEAR FUNCION EN PRUEBAS.PY
    def cartas_jugables(self, cartas):
        """retornar cartas que se pueden jugar de un conjunto de cartas dependiendo del contexto"""
        if not self.context:
            return cartas
        else:
            ultima_carta = self.context[0] #primera carta
            ultimo_triunfo_mas_alto = max(list(filter(lambda carta :carta[1] == self.triunfo)))

            cumplen_regla_1 = list(filter(lambda carta :carta[0]>=ultima_carta[0] and carta[1] == ultima_carta[1]), cartas) #regla1 (mayor del mismo palo)
            cumplen_regla_2 = list(filter(lambda carta :carta[1] == ultima_carta[1])) #regla2   (mismo palo)
            cumplen_regla_3_0 = list(filter(lambda carta :carta[0]>=ultimo_triunfo_mas_alto[0] and carta[1] == self.triunfo)) #regla3.0 (hay triunfo mas alto que el anterior)
            cumplen_regla_3_1 = list(filter(lambda carta :carta[1] == self.triunfo)) #regla3.1 (hay triunfo)

            if cumplen_regla_1:
                return cumplen_regla_1
            elif cumplen_regla_2:
                return cumplen_regla_2
            elif self.fallo and cumplen_regla_3_0:
                return cumplen_regla_3_0
            elif cumplen_regla_3_1:
                return cumplen_regla_3_1
            else:
                return cartas



        





        


jugadores = ["pablo", "cristian", "soledad", "mati"]
jugadores = [Jugador(i) for i in jugadores]
juego = Juego(jugadores)
print(juego.cartas_sin_triunfo)
print("")
print(juego.mazo)
print("")
print(juego.lista_rondas)