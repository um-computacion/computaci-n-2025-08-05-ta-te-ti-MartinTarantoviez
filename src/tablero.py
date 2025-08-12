class Tablero:
    def __init__(self):
        self.casillas = [[" " for _ in range(3)] for _ in range(3)]

    def mostrar(self):
        print("   0   1   2")
        for i, fila in enumerate(self.casillas):
            print(f"{i}  " + " | ".join(fila))
            if i < 2:
                print("  ---+---+---")

    def colocar_ficha(self, fila, columna, ficha):
        if self.casillas[fila][columna] == " ":
            self.casillas[fila][columna] = ficha
            return True
        return False

    def verificar_ganador(self, ficha):
        # Filas y columnas
        for i in range(3):
            if all(self.casillas[i][j] == ficha for j in range(3)):
                return True
            if all(self.casillas[j][i] == ficha for j in range(3)):
                return True
        # Diagonales
        if all(self.casillas[i][i] == ficha for i in range(3)):
            return True
        if all(self.casillas[i][2 - i] == ficha for i in range(3)):
            return True
        return False

    def tablero_lleno(self):
        return all(c != " " for fila in self.casillas for c in fila)
