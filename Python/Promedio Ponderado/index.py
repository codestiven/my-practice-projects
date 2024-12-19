#  Reto: Simulador de una Calculadora de "Notas" (Promedio Ponderado)

class Asignatura:
    def __init__(self, nombre ,calificación, peso):
        self.nombre = nombre
        self.calificación  = calificación
        self.peso = peso


def num_input(string):
    while True:
        try:
            num_asignaturas = int(input(string))
            return num_asignaturas  # Retorna un número entero
        except:
            print("Debe ingresar un número válido.")

def decimal_input(string):
    while True:
        try:
            num_asignaturas = float(input(string))
            return num_asignaturas  # Retorna un número entero
        except:
            print("Debe ingresar un número válido.")



num_asignatura =  num_input("Ingrese el número de Asignaturas: ");


asignaturas = []
for i in range(num_asignatura):
    nombre = input(f"Ingrese el nombre de la asignatura {i+1}: ")
    Calificación = decimal_input("Ingrese la calificación de la asignatura: ")
    peso = decimal_input("Ingrese el peso de la asignatura: ")
    asignatura = Asignatura(nombre  ,Calificación, peso)
    asignaturas.append(asignatura)
    

promedio_ponderado = sum(a.calificación * a.peso for a in asignaturas) / sum(a.peso for a in asignaturas)


print(f"El promedio ponderado es: {promedio_ponderado}")
if promedio_ponderado >= 5:
    print("Aprobado")
else:
    print("Desaprobado")
