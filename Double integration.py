import numpy as np

def simpson_double(f, a, b, c, d, nx, ny):
    if nx % 2 != 0 or ny % 2 != 0:
        raise ValueError("nx and ny MUST be even for Simpson's rule.")

    hx = (b - a) / nx
    hy = (d - c) / ny

    x_vals = [a + i * hx for i in range(nx + 1)]
    y_vals = [c + j * hy for j in range(ny + 1)]

    def simpson_weight(i, n):
        if i == 0 or i == n:
            return 1
        elif i % 2 == 1:
            return 4
        else:
            return 2

    total = 0.0
    for i in range(nx + 1):
        for j in range(ny + 1):
            total += simpson_weight(i, nx) * simpson_weight(j, ny) * f(x_vals[i], y_vals[j])

    return total * (hx * hy) / 9.0



if __name__ == "__main__":
    def f(x, y):
        return x * y

    result = simpson_double(f, a=0, b=2, c=0, d=2, nx=10, ny=10)
    print("Approximate value of double integral =", result)
