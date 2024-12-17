# crea un programa que valide si una targeta de credito es real o no 
#https://www.youtube.com/shorts/IqEkF5iuI-M

def luhn_algorithm(targeta):
    confirmacion = [int(x) for x in str(targeta)][::-1]

    for i in range(len(confirmacion)):
        if i % 2 != 0: 
            confirmacion[i] *= 2
            if confirmacion[i] > 9:
                confirmacion[i] -= 9
    total = sum(confirmacion)
    return total % 10 == 0

entrada = int(input("Introduce una targeta de credito: "))


print(luhn_algorithm(entrada)) 
