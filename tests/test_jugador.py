import unittest
from src.jugador import Jugador

class TestJugador(unittest.TestCase):
    
    def setUp(self):
        self.jugador_x = Jugador("Ana", "X")
        self.jugador_o = Jugador("Luis", "O")
    
    def test_inicializacion(self):
        for jugador, nombre, ficha in [(self.jugador_x, "Ana", "X"), (self.jugador_o, "Luis", "O")]:
            with self.subTest(jugador=nombre):
                self.assertEqual(jugador.nombre, nombre)
                self.assertEqual(jugador.ficha, ficha)
        self.assertEqual(self.jugador_x.fichas_colocadas, 0)
        self.assertEqual(self.jugador_x.max_fichas, 3)
    
    def test_puede_colocar_y_colocar_ficha(self):
        # Coloca fichas hasta el máximo
        for i in range(3):
            self.assertTrue(self.jugador_x.puede_colocar())
            self.assertTrue(self.jugador_x.colocar_ficha())
            self.assertEqual(self.jugador_x.fichas_colocadas, i + 1)
        self.assertFalse(self.jugador_x.puede_colocar())
        self.assertFalse(self.jugador_x.colocar_ficha())
    
    def test_jugadores_independientes(self):
        for _ in range(2): self.jugador_x.colocar_ficha()
        self.jugador_o.colocar_ficha()
        self.assertEqual(self.jugador_x.fichas_colocadas, 2)
        self.assertEqual(self.jugador_o.fichas_colocadas, 1)
        self.assertTrue(self.jugador_x.puede_colocar())
        self.assertTrue(self.jugador_o.puede_colocar())

if __name__ == '__main__':
    unittest.main()
