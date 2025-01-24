import threading
import time
import random

# Stiven De La Rosa Brito #20220457
class Juego:
    def __init__(self, nombre):
        self.nombre = nombre

    def jugar(self):
        for _ in range(5):
            print(f"{self.nombre}: Jugando...")
            time.sleep(random.randint(1, 3))

def ingresar_datos_jugador():
    nombre = input("Ingrese su nombre: ")
    id_jugador = input("Ingrese su número de identificación: ")
    print(f"Bienvenido, {nombre} ({id_jugador})")
    print("Jugador identificado como Stiven de la rosa #20220457")
    return nombre, id_jugador

def ejecutar_juegos(juegos):
    threads = []
    for juego in juegos:
        thread = threading.Thread(target=juego.jugar)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    print("Bienvenido a la simulación de juegos")

    nombre_jugador, id_jugador = ingresar_datos_jugador()

    juegos = [Juego("Halo"), Juego("Overwatch"), Juego("Fallout")]

    ejecutar_juegos(juegos)

    print("Gracias por jugar.")
