import random


class Ronda:
    def __init__(self, cartas_por_jugador, jugador_mano, jugadores, mazo):
        # set
        self.mazo = mazo  # lista de cartas -> (int,str)
        self.jugadores = jugadores  # lista de Jugadores
        self.jugador_mano = jugador_mano  # Jugador
        self.jugador_pie = self.jugadores[
            self.jugadores.index(jugador_mano) - 1
        ]  # Jugador
        self.cartas_por_jugador = cartas_por_jugador  # int de la ronda
        self.ganadores = []
        self.perdedores = []

        # variables temporales, se reasignan en cada mano
        self.triunfo = None  # string del palo
        self.context = []  # historial de cartas jugadas

        ##########
        # execution:
        ##########

        # pre-Game
        self.mezclar()
        self.repartir()
        self.set_triunfo()
        self.pedir_manos()
        self.jugar_ronda()
        self.puntuar()
        self.reset_players()

    def mezclar(self):  # set self.mazo
        random.shuffle(self.mazo)
        print("mazo mezclado")

    def repartir(self):  # set jugadores.cartas
        for _ in range(self.cartas_por_jugador):
            for j in self.jugadores:
                carta = self.mazo.pop(0)
                j.cartas.append(carta)
        print("cartas repartidas")

    def set_triunfo(self):  # set self.triunfo
        if self.mazo:
            self.triunfo = self.mazo.pop(0)[1]
        print(f"triunfo: {self.triunfo}")

    def pedir_manos(self):  # set jugadores.manos_pedidas()
        suma_de_manos_pedidas = 0
        for j in self.jugadores:
            # funcion limite de cartas a pedir
            posibles = list(range(0, self.cartas_por_jugador + 1))
            if (j == self.jugador_pie) and (
                suma_de_manos_pedidas <= self.cartas_por_jugador
            ):  # restriccion
                restriccion = self.cartas_por_jugador - suma_de_manos_pedidas
                posibles.remove(restriccion)

            j.pedir_manos(posibles)

            suma_de_manos_pedidas += j.manos_pedidas

    def jugar_ronda(self):
        jugador_inicial = 0  # index
        for _ in range(self.cartas_por_jugador):
            for j in (
                self.jugadores[jugador_inicial:] + self.jugadores[:jugador_inicial]
            ):
                cartas = j.cartas
                jugables = self.cartas_jugables(cartas)
                carta_jugada = j.turno(jugables)
                self.context.append(carta_jugada)

            carta_ganadora = self.carta_ganadora(self.context)
            for j in self.jugadores:
                if j.carta_tirada == carta_ganadora:
                    ganador = j
            index_ganador = self.jugadores.index(ganador)
            jugador_inicial = index_ganador

            self.jugadores[index_ganador].manos_ganadas.append(self.context)
            print(f"cartas jugadas:\n {self.context}")
            print(
                f"{self.jugadores[index_ganador]} se lleva la mano con {carta_ganadora}"
            )

    def cartas_jugables(self, cartas_disponibles):  # -> list de cartas
        """retorna las cartas jugables dado una lista de cartas y un contexto"""
        if not self.context:
            return cartas_disponibles

        mano_actual = max(
            list(filter(lambda carta: carta[1] == self.context[0][1], self.context))
        )
        triunfos = list(filter(lambda carta: carta[1] == self.triunfo, self.context))
        ultimo_triunfo_mas_alto = (
            max(triunfos) if triunfos else None
        )  # triunfo mas alto tirado

        # regla1 (mayor del mismo palo)
        cumplen_regla_1 = list(
            filter(
                lambda carta: (carta[0] >= mano_actual[0])
                and (carta[1] == mano_actual[1]),
                cartas_disponibles,
            )
        )

        # regla2   (mismo palo)
        cumplen_regla_2 = list(
            filter(lambda carta: (carta[1] == mano_actual[1]), cartas_disponibles)
        )

        if triunfos:
            # regla3.0 (hay triunfo mas alto que el anterior)
            cumplen_regla_3 = list(
                filter(
                    lambda carta: (carta[0] >= ultimo_triunfo_mas_alto[0])
                    and (carta[1] == self.triunfo),
                    cartas_disponibles,
                )
            )

        # regla4 (hay triunfo)
        cumplen_regla_4 = list(
            filter(lambda carta: (carta[1] == self.triunfo), cartas_disponibles)
        )

        if not self.context:  # si no hay cartas entonces soy el primero
            return cartas_disponibles

        if cumplen_regla_1:
            return cumplen_regla_1
        elif cumplen_regla_2:
            return cumplen_regla_2
        elif triunfos and cumplen_regla_3:
            return cumplen_regla_3
        elif cumplen_regla_4:
            return cumplen_regla_4
        else:
            return cartas_disponibles

    def carta_ganadora(self, cartas_tiradas):  # -> carta
        """retorna la carta ganadora de una mano dada una lista de cartas tiradas"""

        triunfos = list(filter(lambda carta: carta[1] == self.triunfo, cartas_tiradas))
        palo_principal = list(
            filter(lambda carta: carta[1] == cartas_tiradas[0][1], cartas_tiradas)
        )

        if triunfos:  # si hay cartas con triunfo
            return max(triunfos)
        else:
            return max(palo_principal)

    def puntuar(self):  # set jugadores.puntos
        """asigna puntaje a los jugadores"""

        for j in self.jugadores:
            puntos = 0
            manos_ganadas = len(j.manos_ganadas)
            manos_pedidas = j.manos_pedidas
            if manos_pedidas == manos_ganadas:
                puntos += 10
                self.ganadores.append(j)
            else:
                self.perdedores.append(j)
            puntos += manos_ganadas
            j.puntos = puntos

        print("ganadores: {}".format(self.ganadores))
        print("perdedores: {}".format(self.perdedores))

    def reset_players(self):
        for j in self.jugadores:
            j.reset_temp_variables()
