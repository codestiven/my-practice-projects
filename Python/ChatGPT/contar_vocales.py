
"""
Ejercicio:

Escribe una función en Python llamada contar_vocales que reciba una cadena de texto y devuelva el número de vocales (a, e, i, o, u) que contiene. No se debe diferenciar entre mayúsculas y minúsculas.

Ejemplo:

python
Copiar código
print(contar_vocales("Hola Mundo"))  # Debería imprimir 4
print(contar_vocales("Python es divertido"))  # Debería imprimir 6
Recuerda pensar en cómo manejar tanto las mayúsculas como las minúsculas y en cómo iterar sobre cada carácter de la cadena para contar las vocales.

"""




def contar_vocales(palabra):
    cantidad = 0
    palabra = palabra.lower()
    
    
    for letra in palabra:
        if letra in 'aeiou':
            cantidad += 1


    return cantidad
    
salida = input("ingrese una palabra :")
print(contar_vocales(salida))

# ** ¡Buen trabajo con la función! Si necesitas más ayuda o quieres más ejercicios, avísame.