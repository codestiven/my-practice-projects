#generador de contrasena aleatoria

import random



def generar_contrasena():
    num_characters = random.randint(8,12)
    caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%'
    password = ""

    #cantidad de caracteres
    for i in range(num_characters):
        #se genera un numero aleatorio para seleccionar un caracter
        password += caracteres[random.randint(0,(len(caracteres)-1))]

    return password

print(generar_contrasena())