import math

x = 0.0
while x <= 10:
    sin_x = math.sin(x)
    cos_x = math.cos(x)
    tan_x = math.tan(x)
    print(f"x: {x} \t sin(x): {sin_x:.4f} \t cos(x): {cos_x:.4f} \t tan(x): {tan_x:.4f}")
    x += 0.2
