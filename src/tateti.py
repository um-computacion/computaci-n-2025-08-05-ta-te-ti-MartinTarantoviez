from src.tablero import Tablero
from src.jugador import Jugador
from src.CLI import pedir_posicion, mostrar_mensaje

def jugar():
    tablero = Tablero()
    jugador1 = Jugador("Jugador 1", "X")
    jugador2 = Jugador("Jugador 2", "O")
    jugadores = [jugador1, jugador2]

    turno = 0
    while True:
        jugador_actual = jugadores[turno % 2]
        tablero.mostrar()
        mostrar_mensaje(f"Turno de {jugador_actual.nombre} ({jugador_actual.ficha})")

        while True:
            fila, columna = pedir_posicion()
            if fila is None and columna is None:
                mostrar_mensaje("Juego terminado por el usuario.")
                return  # Sale de la función y termina la partida

            if tablero.colocar_ficha(fila, columna, jugador_actual.ficha):
                break
            else:
                mostrar_mensaje("Casilla ocupada. Intenta nuevamente.")

        if tablero.verificar_ganador(jugador_actual.ficha):
            tablero.mostrar()
            mostrar_mensaje(f"¡{jugador_actual.nombre} gana!")
            break

        if tablero.tablero_lleno():
            tablero.mostrar()
            mostrar_mensaje("¡Empate!")
            break

        turno += 1

if __name__ == "__main__":
    jugar()
