def pedir_posicion():
    while True:
        try:
            entrada_fila = input("Ingrese fila (0-2 o 'q' para salir): ").strip().lower()
            if entrada_fila in ["q", "salir"]:
                return None, None  # Señal de que se quiere salir

            fila = int(entrada_fila)

            entrada_columna = input("Ingrese columna (0-2 o 'q' para salir): ").strip().lower()
            if entrada_columna in ["q", "salir"]:
                return None, None

            columna = int(entrada_columna)

            if 0 <= fila <= 2 and 0 <= columna <= 2:
                return fila, columna
            else:
                print("Fila y columna deben estar entre 0 y 2.")
        except ValueError:
            print("Por favor ingrese números válidos o 'q' para salir.")

def mostrar_mensaje(msg):
    print(msg)
