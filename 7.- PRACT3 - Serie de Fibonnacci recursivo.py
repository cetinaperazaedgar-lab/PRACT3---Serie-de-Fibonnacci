def fibonacci_recursivo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

n = int(input("¿Cuántos términos de la serie de Fibonacci deseas ver? "))

print("Serie de Fibonacci (recursiva):")
for i in range(n):
    print(f"F({i}) = {fibonacci_recursivo(i)}")
