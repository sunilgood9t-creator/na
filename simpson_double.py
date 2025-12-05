import numpy as np

def simpson_double(f, a, b, c, d, N_x, N_y):
    # 1. Check for even number of intervals
    if N_x % 2 != 0 or N_y % 2 != 0:
        raise ValueError("Both N_x and N_y (number of intervals) must be even for Simpson's 1/3 Rule.")
    
    # 2. Calculate interval widths (h and k)
    h_x = (b - a) / N_x
    h_y = (d - c) / N_y
    
    total = 0.0
    
    # 3. Outer loop for x (variable i)
    for i in range(N_x + 1):
        x = a + i * h_x
        
        # Determine Simpson's weight for x-direction (wx)
        if i == 0 or i == N_x:
            wx = 1.0
        elif i % 2 == 1: # Odd index (1, 3, 5, ...)
            wx = 4.0
        else:          # Even index (2, 4, 6, ...)
            wx = 2.0
            
        # 4. Inner loop for y (variable j) - MUST BE NESTED!
        for j in range(N_y + 1):
            y = c + j * h_y
            
            # Determine Simpson's weight for y-direction (wy)
            if j == 0 or j == N_y:
                wy = 1.0
            elif j % 2 == 1: # Odd index
                wy = 4.0
            else:          # Even index
                wy = 2.0
                
            # 5. Accumulate the weighted function value
            # The total weight for the point (x,y) is wx * wy
            total += wx * wy * f(x, y)
            
    # 6. Apply the final scaling factor (h_x/3 * h_y/3 = h_x*h_y/9)
    result = (h_x * h_y / 9.0) * total
    return result

# Example Usage:
f = lambda x, y: x**2 + y**2 + 2
# The exact integral for this function from 0 to 1 in both x and y is:
# Integral((x^2 + y^2 + 2) dy dx) = [x^2*y + y^3/3 + 2y]_0^1 dx = (x^2 + 1/3 + 2) dx = (x^2 + 7/3) dx
# = [x^3/3 + 7x/3]_0^1 = 1/3 + 7/3 = 8/3 = 2.66666...

# Use N_x=6 and N_y=6 intervals (even and accurate)
N_x = 6
N_y = 6
result = simpson_double(f, 0, 1, 0, 1, N_x, N_y)

print(f"Number of Intervals (Nx, Ny): ({N_x}, {N_y})")
print(f"Approximate Integral: {result}")
print(f"Exact Value (8/3): {8/3}")
