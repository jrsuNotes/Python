def generate_fibonacci(n):
    fibonacci_series = []

    # First two terms of the series
    fibonacci_series.append(0)
    fibonacci_series.append(1)

    for i in range(2, n):
        next_term = fibonacci_series[i-1] + fibonacci_series[i-2]
        fibonacci_series.append(next_term)

    return fibonacci_series

# Example usage:
num_terms = int(input("Enter the number of Fibonacci terms to generate: "))

fibonacci_sequence = generate_fibonacci(num_terms)
print("Fibonacci Series:", fibonacci_sequence)
