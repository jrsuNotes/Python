import math

def calculate_series(n):
    result = 1.0  # Start with the initial value of 1

    for i in range(1, n+1):
        factorial = math.factorial(i)
        term = 1 / factorial
        result += term

    return result

# Example usage:
n = int(input("Enter a value for n: "))
series_sum = calculate_series(n)
print("Sum of the series:", series_sum)
