# kirito = int(input("ingrese la fuerza iniciar de kirito :"))
# dragon = 0
# cantida_dragones = int(input("ingrese la cantidad de dragones :"))

# for i in range(1, cantida_dragones):
#     dragon = int(input("nivel del dragon :"))
#     if dragon < kirito :
#         kirito = kirito + dragon
#         print("si")
#     else:
#         print("no")
#         break


# Ingresar los valores enteros separados por espacios
dragones = input("Ingresa los valores enteros separados por espacios: ")

# Dividir los valores ingresados en una lista
valores = valores_entrada.split()

# Convertir los valores a enteros y crear una lista ordenada
lista_enteros = sorted([int(valor) for valor in valores])

# Imprimir la lista ordenada
print("Lista ordenada de menor a mayor:", lista_enteros)
