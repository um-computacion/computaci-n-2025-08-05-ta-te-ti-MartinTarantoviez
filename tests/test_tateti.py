import unittest
from unittest.mock import patch
import sys
import os

# Ajustar path para importar src
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.tablero import Tablero
from src.jugador import Jugador
from src.CLI import pedir_posicion, mostrar_mensaje


class TestTablero(unittest.TestCase):

    def setUp(self):
        self.tablero = Tablero()

    def test_inicializacion_y_colocar_ficha(self):
        # Tablero inicial vacío
        for fila in self.tablero.casillas:
            for celda in fila:
                self.assertEqual(celda, " ")
        # Colocar ficha válida
        self.assertTrue(self.tablero.colocar_ficha(0, 0, "X"))
        self.assertEqual(self.tablero.casillas[0][0], "X")
        # Intentar ocupar casilla ya usada
        self.assertFalse(self.tablero.colocar_ficha(0, 0, "O"))

    def test_verificar_ganador(self):
        # Filas, columnas y diagonales
        for j in range(3):
            self.tablero.casillas[0][j] = "X"
        self.assertTrue(self.tablero.verificar_ganador("X"))
        self.assertFalse(self.tablero.verificar_ganador("O"))

        self.tablero = Tablero()
        for i in range(3):
            self.tablero.casillas[i][0] = "O"
        self.assertTrue(self.tablero.verificar_ganador("O"))

        self.tablero = Tablero()
        for i in range(3):
            self.tablero.casillas[i][i] = "X"
        self.assertTrue(self.tablero.verificar_ganador("X"))

        self.tablero = Tablero()
        for i in range(3):
            self.tablero.casillas[i][2 - i] = "O"
        self.assertTrue(self.tablero.verificar_ganador("O"))

        # Sin ganador
        self.tablero = Tablero()
        self.tablero.casillas[0][0] = "X"
        self.tablero.casillas[1][1] = "O"
        self.assertFalse(self.tablero.verificar_ganador("X"))
        self.assertFalse(self.tablero.verificar_ganador("O"))

    def test_tablero_lleno(self):
        fichas = ["X", "O"] * 5
        idx = 0
        for i in range(3):
            for j in range(3):
                self.tablero.casillas[i][j] = fichas[idx]
                idx += 1
        self.assertTrue(self.tablero.tablero_lleno())

        self.tablero.casillas[0][0] = " "
        self.assertFalse(self.tablero.tablero_lleno())

    @patch('builtins.print')
    def test_mostrar(self, mock_print):
        self.tablero.mostrar()
        mock_print.assert_called()


class TestJugador(unittest.TestCase):

    def setUp(self):
        self.jugador = Jugador("Test", "X")

    def test_inicializacion_y_colocar_ficha(self):
        self.assertEqual(self.jugador.nombre, "Test")
        self.assertEqual(self.jugador.ficha, "X")
        self.assertEqual(self.jugador.fichas_colocadas, 0)
        self.assertTrue(self.jugador.puede_colocar())

        for i in range(3):
            self.assertTrue(self.jugador.colocar_ficha())
            self.assertEqual(self.jugador.fichas_colocadas, i + 1)
        self.assertFalse(self.jugador.puede_colocar())
        self.assertFalse(self.jugador.colocar_ficha())


class TestCLI(unittest.TestCase):

    @patch('builtins.input')
    def test_pedir_posicion_validas(self, mock_input):
        casos = [
            (['1', '2'], (1, 2)),
            (['0', '0'], (0, 0)),
            (['2', '2'], (2, 2)),
            ([' 1 ', ' 2 '], (1, 2)),
        ]
        for entradas, esperado in casos:
            mock_input.side_effect = entradas
            fila, col = pedir_posicion()
            self.assertEqual((fila, col), esperado)

    @patch('builtins.input')
    def test_pedir_posicion_salir(self, mock_input):
        casos = [['q'], ['salir'], ['1', 'q']]
        for entradas in casos:
            mock_input.side_effect = entradas
            fila, col = pedir_posicion()
            self.assertIsNone(fila)
            self.assertIsNone(col)

    @patch('builtins.print')
    @patch('builtins.input')
    def test_pedir_posicion_invalidas(self, mock_input, mock_print):
        casos = [
            (['3', '1', '1', '1'], "Fila y columna deben estar entre 0 y 2."),
            (['1', '-1', '1', '1'], "Fila y columna deben estar entre 0 y 2."),
            (['abc', '1', '1'], "Por favor ingrese números válidos o 'q' para salir."),
            (['1', '2.5', '1', '1'], "Por favor ingrese números válidos o 'q' para salir."),
        ]
        for entradas, msg in casos:
            mock_input.side_effect = entradas
            fila, col = pedir_posicion()
            self.assertEqual((fila, col), (1, 1))
            mock_print.assert_any_call(msg)

    @patch('builtins.print')
    def test_mostrar_mensaje(self, mock_print):
        for msg in ["Mensaje prueba", ""]:
            with self.subTest(msg=msg):
                mostrar_mensaje(msg)
                mock_print.assert_called_with(msg)


if __name__ == '__main__':
    unittest.main(verbosity=2)
