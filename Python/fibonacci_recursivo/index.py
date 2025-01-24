def fibonacci_recursivo(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


n = int(input("Ingresa el valor de 'n' para calcular el enésimo número de Fibonacci: "))


resultado = fibonacci_recursivo(n)
print("El enésimo número de Fibonacci para n =", n, "es:", resultado)
