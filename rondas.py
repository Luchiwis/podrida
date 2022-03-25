import cartas, random

class Ronda:
    def __init__(self, ronda:int, jugadores:list, mazo:list):
        self.mazo = mazo
        self.manos = {j:[] for j in jugadores}      #{jugador:[{carta:jugador, carta:jugador, ...}, {carta:jugador, carta:jugador, ...}], ...}
        self.apuestas = {j:0 for j in jugadores}    #{jugador:apuesta, jugador:apuesta, ...}
        self.puntos = {j:0 for j in jugadores}      #{jugador:puntos, jugador:puntos, ...}
        self.cartas = {j:[] for j in jugadores}     #{jugador:[carta, carta, ...], jugador:[carta, carta, ...], ...}
        self.jugadores = jugadores                  #lista de jugadores
        self.triunfo = False                        #carta triunfo
        self.ronda = ronda                          #numero de ronda actual

    def mezclar(self): #-> list of cartas
        random.shuffle(self.mazo)
        print("mazo mezclado")

    def repartir(self): #set self.cartas
        for _ in range(self.ronda):
            for j in self.cartas.keys():
                carta = self.mazo.pop(0)
                self.cartas[j].append(carta)
        self.triunfo = self.mazo.pop(0)

    def pedir_manos(self,jugador):  #set self.apuestas
        for jugador in self.jugadores:
            jugador.pedir_manos()
            #TODO LIMIT

    def tirar(self, jugador):   #set self.manos
        for _ in range(self.ronda):
            cartas_tiradas = {}
            for jugador in self.jugadores:
                cartas_totales = self.cartas[jugador]
                cartas_disponibles = self.disponibles(cartas_tiradas.keys(), cartas_totales)

                carta_tirada = jugador.tirar_carta(cartas_disponibles, cartas_totales)
                cartas_tiradas[carta_tirada] = jugador
            carta_ganadora = self.carta_ganadora(cartas_tiradas.keys())
            ganador = cartas_tiradas[carta_ganadora]
            self.manos[ganador].append(cartas_tiradas)

    def carta_ganadora(self,cartas_tiradas): #-> carta
        """determina la carta ganadora de una mano dado una lista de cartas tiradas"""
        if self.triunfo.palo in [c.palo for c in cartas_tiradas]:
            return max(filter(lambda x:x.palo == self.triunfo.palo, cartas_tiradas), key=lambda x:x.valor)
        else:
            return max(filter(lambda x:x.palo == cartas_tiradas[0].palo, cartas_tiradas), key=lambda x:x.valor)
        
    def disponibles(self, cartas_tiradas, mis_cartas):  #-> list de cartas
        """retorna las cartas jugables dado una lista de cartas y un contexto"""
        fallo = self.triunfo.palo in [c.palo for c in cartas_tiradas]

        if not cartas_tiradas:
            return mis_cartas
        else:
            for c in mis_cartas:    #4 reglas
                mano_de = cartas_tiradas[0]
                if fallo and (c.palo == mano_de.palo):  #ya fallo y tengo el mismo palo
                    return list(filter(lambda x:x.palo==mano_de.palo, mis_cartas))
                
                elif (c.palo == mano_de.palo) and (c.valor >= mano_de.valor):   #no fallo y tengo el mismo palo y el valor es mayor
                    return list(filter(lambda x:(c.palo == mano_de.palo) and (c.valor >= mano_de.valor), mis_cartas))
                    
                elif (c.palo == mano_de.palo) and (c.valor < mano_de.valor):    #no fallo y tengo el mismo palo y el valor es menor
                    return list(filter(lambda x:(c.palo == mano_de.palo) and (c.valor < mano_de.valor), mis_cartas))

                elif (c.palo == self.triunfo.palo):   #no fallo pero solo tengo triunfo
                    return list(filter(lambda x:c.palo == self.triunfo.palo, mis_cartas))

                else:   #no tengo nada
                    return mis_cartas
            
    def puntuar(self):
        """asigna puntaje a los jugadores los jugadores"""
        for jugador in self.jugadores:
            puntos = 0
            manos_ganadas = self.manos[jugador]
            manos_apostadas = self.apuestas[jugador]
            if manos_apostadas == manos_ganadas:
                puntos +=10
            puntos += len(manos_ganadas)
            self.puntos[jugador] = puntos

mazo = [cartas.Carta(p,v) for v in range(1,13) for p in ["basto","copa","espada","oro"] if v not in [8,9]]
ronda1 = Ronda(1, ["lucio","juan","carlos","lolo"],mazo)
ronda1.mezclar()
ronda1.repartir()
