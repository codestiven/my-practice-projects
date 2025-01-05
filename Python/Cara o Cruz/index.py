# Programa un lanzamiento de cara o cruz que este trucado para que lanzo mas veces cara
import random



# Función que simula el lanzamiento de la moneda
moneda = ["cara", "cruz"]
def lanzar_moneda():
    if random.random() < 0.6:
        return moneda[0]
    else:  
        return moneda[1]

print(lanzar_moneda())