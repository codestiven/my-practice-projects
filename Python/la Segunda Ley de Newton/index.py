# Segunda Ley de Newton: F = m * a

def calcular_fuerza(masa, aceleracion):
    return masa * aceleracion

# Ejemplo de uso
masa = float(input("Ingresa la masa del objeto (kg): "))
aceleracion = float(input("Ingresa la aceleración (m/s^2): "))

fuerza = calcular_fuerza(masa, aceleracion)

print(f"\nLa fuerza aplicada es: {fuerza} N (Newtons)")
