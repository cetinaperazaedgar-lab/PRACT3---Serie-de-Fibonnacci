def fibonacci(n):
    serie = [0, 1] 
    for i in range(2, n):
        serie.append(serie[i-1] + serie[i-2])
    return serie

n = int(input("¿Cuántos términos de la serie de Fibonacci deseas ver? "))

resultado = fibonacci(n)
print("Serie de Fibonacci:")
print(resultado)
