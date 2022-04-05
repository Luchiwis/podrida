class Jugador:
    def __init__(self, name):
        self.nombre = name
        self.puntos = 0

        #en ronda
        self.cartas = []
        self.cartasJugables = []
        self.manos_ganadas = []     #lista de listas de cartas
        self.manos_pedidas = None #int

        #en mano
        self.carta_tirada = None

    def pedir_manos(self, limit):   #set self.manos_pedidas
        manos = int(input("manos: "))
        self.manos_pedidas = manos

    def turno(self,cartas_jugables): # -> carta
        print("seleccionar una carta")
        for i,c in enumerate(cartas_jugables):
            print(f"{i}) {c}")

        i = int(input(":"))
        self.carta_tirada = cartas_jugables.pop(i)
        return self.carta_tirada
    
    def __str__(self):
        return self.nombre

    def __repr__(self):
        return self.__str__()