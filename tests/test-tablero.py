import unittest
from src.tablero import Tablero

class TestTablero(unittest.TestCase):
    
    def setUp(self):
        self.tablero = Tablero()
    
    def test_inicializacion(self):
        for fila in self.tablero.casillas:
            for casilla in fila:
                self.assertEqual(casilla, " ")
    
    def test_colocar_ficha(self):
        # Casilla vacía
        self.assertTrue(self.tablero.colocar_ficha(1, 1, "X"))
        self.assertEqual(self.tablero.casillas[1][1], "X")
        # Casilla ocupada
        self.assertFalse(self.tablero.colocar_ficha(1, 1, "O"))
    
    def test_verificar_ganador(self):
        # Ganador fila
        for col in range(3): self.tablero.colocar_ficha(0, col, "X")
        self.assertTrue(self.tablero.verificar_ganador("X"))
        self.assertFalse(self.tablero.verificar_ganador("O"))
        
        self.tablero = Tablero()
        # Ganador columna
        for fila in range(3): self.tablero.colocar_ficha(fila, 0, "O")
        self.assertTrue(self.tablero.verificar_ganador("O"))
        
        self.tablero = Tablero()
        # Diagonal principal
        for i in range(3): self.tablero.colocar_ficha(i, i, "X")
        self.assertTrue(self.tablero.verificar_ganador("X"))
        
        self.tablero = Tablero()
        # Diagonal secundaria
        for i in range(3): self.tablero.colocar_ficha(i, 2 - i, "O")
        self.assertTrue(self.tablero.verificar_ganador("O"))
        
        self.tablero = Tablero()
        # Sin ganador
        self.tablero.colocar_ficha(0, 0, "X")
        self.tablero.colocar_ficha(1, 1, "O")
        self.assertFalse(self.tablero.verificar_ganador("X"))
        self.assertFalse(self.tablero.verificar_ganador("O"))
    
    def test_tablero_lleno(self):
        self.assertFalse(self.tablero.tablero_lleno())
        # Llenar parcialmente y sigue sin estar lleno
        self.tablero.colocar_ficha(0, 0, "X")
        self.assertFalse(self.tablero.tablero_lleno())
        # Llenar completamente
        fichas = ["X", "O", "X", "O", "X", "O", "X", "O", "X"]
        pos = 0
        for fila in range(3):
            for col in range(3):
                self.tablero.colocar_ficha(fila, col, fichas[pos])
                pos += 1
        self.assertTrue(self.tablero.tablero_lleno())

if __name__ == "__main__":
    unittest.main()
