def a_decimal(numero, base):
    decimal = 0
    numero = str(numero)
    for i, digito in enumerate(numero[::-1]):
        if '0' <= digito <= '9':
            decimal += int(digito) * (base ** i)
        else:
            decimal += (ord(digito.upper()) - ord('A') + 10) * (base ** i)
    return decimal

def de_decimal(decimal, base):
    digitos = "0123456789ABCDEF"
    resultado = ""
    while decimal > 0:
        resultado = digitos[decimal % base] + resultado
        decimal = decimal // base
    return resultado or "0"

def convertir(numero, de_base, a_base):
    decimal = a_decimal(numero, de_base)
    return de_decimal(decimal, a_base)

# Ejemplos de uso
print(convertir("1010", 2, 16))
print(convertir("12", 8, 10))
print(convertir("F", 16, 2))