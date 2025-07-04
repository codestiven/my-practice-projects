import random

# Elige un número aleatorio entre 1 y 10
numero_secreto = random.randint(1, 10)

print("Adivina el número (entre 1 y 10):")

# Pedimos al usuario que adivine
intento = int(input("Tu intento: "))

# Comparamos el intento con el número secreto
if intento == numero_secreto:
    print("¡Correcto! 🎉 Adivinaste el número.")
else:
    print(f"No adivinaste 😞. El número era {numero_secreto}.")
