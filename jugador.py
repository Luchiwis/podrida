class Jugador:
    def __init__(self, name):
        self.nombre = name
        self.puntos = 0

        # en ronda
        self.reset_temp_variables()

        # en mano
        self.carta_tirada = None

    def say_name(self):
        print(f"\n{self.nombre}")

    def reset_temp_variables(self):
        self.cartas = []
        self.cartasJugables = []
        self.manos_ganadas = []  # lista de listas de cartas
        self.manos_pedidas = None  # int

    def pedir_manos(self, posibles):  # set self.manos_pedidas
        self.say_name()
        print("cuantas manos pedis?")
        print(f"cartas: {self.cartas}")
        for i in posibles:
            print(f"{i})")

        i = int(input(":"))
        assert i in posibles
        self.manos_pedidas = i

    def turno(self, cartas_jugables):  # -> carta
        self.say_name()
        print("seleccionar una carta")
        for i, c in enumerate(cartas_jugables):
            print(f"{i}) {c}")

        i = int(input(":"))
        self.carta_tirada = cartas_jugables.pop(i)
        return self.carta_tirada

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return self.__str__()
