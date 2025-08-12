import unittest
from unittest.mock import patch
import io
import sys
from src.CLI import pedir_posicion, mostrar_mensaje

class TestCli(unittest.TestCase):

    @patch('builtins.input')
    def test_pedir_posicion_validas(self, mock_input):
        # Probamos varias entradas válidas y que retornan correctamente
        casos = [
            (['1', '2'], (1, 2)),
            (['0', '0'], (0, 0)),
            (['2', '2'], (2, 2)),
            ([' 1 ', ' 2 '], (1, 2)),
        ]
        for entradas, esperado in casos:
            mock_input.side_effect = entradas
            fila, columna = pedir_posicion()
            self.assertEqual((fila, columna), esperado)

    @patch('builtins.input')
    def test_pedir_posicion_salir(self, mock_input):
        # Probar salida con 'q' o 'salir'
        casos = [
            (['q'], (None, None)),
            (['salir'], (None, None)),
        ]
        for entradas, esperado in casos:
            mock_input.side_effect = entradas
            fila, columna = pedir_posicion()
            self.assertEqual((fila, columna), esperado)

    @patch('builtins.input')
    @patch('builtins.print')
    def test_pedir_posicion_entradas_invalidas(self, mock_print, mock_input):
        # Probar inputs inválidos seguidos de válidos para validar mensajes de error
        casos = [
            (['3', '1', '1', '1'], "Fila y columna deben estar entre 0 y 2."),
            (['1', '-1', '1', '1'], "Fila y columna deben estar entre 0 y 2."),
            (['abc', '1', '1'], "Por favor ingrese números válidos o 'q' para salir."),
            (['1', '2.5', '1', '1'], "Por favor ingrese números válidos o 'q' para salir."),
        ]
        for entradas, mensaje_esperado in casos:
            mock_input.side_effect = entradas
            fila, columna = pedir_posicion()
            self.assertEqual((fila, columna), (1,1))
            mock_print.assert_any_call(mensaje_esperado)

    def test_mostrar_mensaje(self):
        # Captura de salida estándar para validar imprimir mensajes
        for mensaje in ["Mensaje de prueba", ""]:
            with self.subTest(mensaje=mensaje):
                captured_output = io.StringIO()
                sys.stdout = captured_output
                mostrar_mensaje(mensaje)
                sys.stdout = sys.__stdout__
                self.assertEqual(captured_output.getvalue().strip(), mensaje)

if __name__ == '__main__':
    unittest.main()
