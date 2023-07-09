def calculate_gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp

    return a

# Example usage:
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

gcd = calculate_gcd(num1, num2)
print("GCD of", num1, "and", num2, "is:", gcd)
