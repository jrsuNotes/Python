def calculate_factorial(n):
    factorial = 1

    if n < 0:
        print("Factorial is not defined for negative numbers.")
        return None
    elif n == 0:
        return factorial
    else:
        for i in range(1, n + 1):
            factorial *= i
        return factorial

# Example usage:
n = int(input("Enter a number: "))
factorial = calculate_factorial(n)

if factorial is not None:
    print("Factorial:", factorial)
