# verificar si una palabra es de palindromos

palabra = input("Ingrese una palabra: ")

def verificar_palindromo(palabra):
    palabra = palabra.lower()
    palabra = palabra.replace(" ", "")
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


if verificar_palindromo(palabra):
    print("La palabra es un palindromo")
else:
    print("La palabra no es un palindromo")