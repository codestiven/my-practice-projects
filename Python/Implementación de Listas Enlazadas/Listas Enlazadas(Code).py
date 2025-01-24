"""

@ Stiven De La Rosa Brito --------------------------------------------------------
@ 20220457 --------------------------------------------------------
@ 3/2/2024 --------------------------------------------------------

"""



import os # agrega opciones de limpieza

from colorama import Fore, Style, init  # para agregar color


# creaccion de la clase para crear nodos

class Nodo:
    def __init__(self , nombre_cancion):
        self.nombre_cancion = nombre_cancion
        self.siguiente = None


# clase para representar la lista de reproducción

class Lista_de_reproduccion:
    def __init__(self):
        self.cancion_actual = None
    # Método para agregar una canción

    def reproducir_cancion(self, nombre):
        nueva_cancion = Nodo(nombre)
        nueva_cancion.siguiente = self.cancion_actual
        self.cancion_actual = nueva_cancion

    # Método para ir a la siguiente
    def siguiente_cancion(self):
        if self.cancion_actual != None:
            self.cancion_actual = self.cancion_actual.siguiente

    # Método para mostrar la lista
    def mostrar_lista(self):
        actual = self.cancion_actual
        while actual:
            print(f"{Fore.BLUE}{actual.nombre_cancion}{Style.RESET_ALL}", end=" -> ")
            actual = actual.siguiente
        print("Null")
    # Método para eliminar una canción
    def eliminar_cancion(self, nombre):
        actual = self.cancion_actual
        anterior = None

        while actual and actual.nombre_cancion != nombre:
            anterior = actual
            actual = actual.siguiente
        # Si la cancion existe
        if actual:
            if anterior:
                anterior.siguiente = actual.siguiente
            else:
                self.cancion_actual = actual.siguiente
        # Si la cancion no existe
        else:
            print(f"{Fore.RED}La cancion '{nombre}' no existe en la lista.{Style.RESET_ALL}")

# Función para limpiar la consola
def Clear():
    os.system("cls")
# Función principal 
def interactuar():
    lista_reproduccion = Lista_de_reproduccion()
    while True:
        Clear()
        # Mostrar opciones
        print(f"\n{Fore.YELLOW}Lista de reproduccion{Style.RESET_ALL}")
        print(f"\n{Fore.GREEN}1. Agregar cancion")
        print(f"{Fore.RED}2. Eliminar cancion")
        print(f"{Fore.YELLOW}3. Mostrar lista")
        print(f"{Fore.BLUE}4. Salir{Style.RESET_ALL}")
        # Solicitar opción 
        Entrada = input("Ingrese una Entrada: ")
        # hacer la opción seleccionada
        if Entrada == "1":
            nombre_cancion = input(f"{Fore.CYAN}Ingrese el nombre de la cancion:{Style.RESET_ALL} ")
            lista_reproduccion.reproducir_cancion(nombre_cancion)
        elif Entrada == "2":
            # Mostrar lista actual para eliminar
            print(f"\n{Fore.RED}Lista de canciones a borrar:{Style.RESET_ALL}")
            lista_reproduccion.mostrar_lista()
            nombre_cancion = input(f"\n{Fore.RED}Ingrese el nombre de la cancion a {Fore.RED}eliminar{Style.RESET_ALL}:{Style.RESET_ALL} ")
            lista_reproduccion.eliminar_cancion(nombre_cancion)
            input(f"\nPresione Enter para continuar...")
        elif Entrada == "3":
            # Mostrar lista actual
            print(f"\n{Fore.YELLOW}Lista de reproducción actual:{Style.RESET_ALL}")
            lista_reproduccion.mostrar_lista()
            input(f"\nPresione Enter para continuar...")
        elif Entrada == "4":
            break
            #termmina programa
        else:
            # Mensaje de error 
            print(f"{Fore.YELLOW}Opción no valida. Intentelo de nuevo.{Style.RESET_ALL}")
            input(f"\nPresione Enter para continuar...")


if __name__ == "__main__":
    init(autoreset=True)  # comenzar colorama 
    interactuar() # Llamar la función para iniciar el programa

