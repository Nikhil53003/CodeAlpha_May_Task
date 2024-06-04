def fibonacci_sequence(n):
    """Generate a list of the first n Fibonacci numbers."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence

n = int(input("Enter the number of Fibonacci numbers to generate: "))
fib_sequence = fibonacci_sequence(n)
print(f"The first {n} Fibonacci numbers are: {fib_sequence}")