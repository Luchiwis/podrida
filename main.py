import cartas

palos = ["basto","espada","oro","copa"]

mazo = [cartas.Carta(palo, numero) for numero in range(1, 13) for palo in self.palos]
