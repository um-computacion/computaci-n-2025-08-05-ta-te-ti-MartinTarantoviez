class Jugador:
    def __init__(self, nombre, ficha):
        self.nombre = nombre
        self.ficha = ficha  # "X" o "O"
        self.fichas_colocadas = 0
        self.max_fichas = 3

    def puede_colocar(self):
        return self.fichas_colocadas < self.max_fichas

    def colocar_ficha(self):
        if self.puede_colocar():
            self.fichas_colocadas += 1
            return True
        return False
