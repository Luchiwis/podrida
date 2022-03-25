class Jugador:
    def __init__(self, name):
        self.nombre = name
        self.puntos = 0

        #en ronda
        self.cartas = []
        self.cartasJugables = []
        self.manos_ganadas = []     #lista de listas
        self.manos_pedidas = None #int

    def pedir_manos(self, limit):   #set self.manos_pedidas
        manos = int(input("manos: "))
        self.manos_pedidas = manos

    def turno(self,cartas_jugables):
        pass

    def tirar_carta(self,carta):
        pass
    
    def __str__(self):
        return self.nombre

    def __repr__(self):
        return self.__str__()