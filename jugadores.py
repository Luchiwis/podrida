import cartas
class Jugador:
    def __init__(self,id,nombre):
        self.id = id
        self.nombre = nombre
    
    def pedir_manos(self, limit):
        manos = int(input("manos: "))
        return manos
    
    def tirar_carta(self,disponibles, totales):
        carta = cartas.Carta("basto",1)
        return carta
    
    def __str__(self):
        return self.nombre

    def __repr__(self):
        return self.__str__()
