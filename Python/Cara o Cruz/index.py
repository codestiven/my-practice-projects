import random

# Función que simula el lanzamiento de la moneda
moneda = ["cara", "cruz"]
def lanzar_moneda():
    if random.random() < 0.6:  # Probabilidad de 60% para "cara"
        return moneda[0]
    else:  
        return moneda[1]


print(f"ha salido {lanzar_moneda()}")
caras = 0
cruces = 0

# Realizar los lanzamientos
for i in range(1000000):
    if lanzar_moneda() == "cara":
        caras += 1
    else:
        cruces += 1

# Calcular porcentajes
total = caras + cruces
porcentaje_caras = (caras / total) * 100
porcentaje_cruces = (cruces / total) * 100

# Mostrar resultados
print("Caras:", caras, "Cruces:", cruces)
print(f"Porcentaje de caras: {porcentaje_caras:.2f}%")
print(f"Porcentaje de cruces: {porcentaje_cruces:.2f}%")
