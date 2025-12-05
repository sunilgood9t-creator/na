def gauss_seidel(A, b, tol=1e-10, max_iter=1000):

    n = len(A)

    x = [0.0 for _ in range(n)]
    
    for iteration in range(max_iter):
        x_old = x.copy()
        
        for i in range(n):
            sigma = 0
            for j in range(n):
                if j != i:
                    sigma += A[i][j] * x[j]
            x[i] = (b[i] - sigma) / A[i][i]

        diff = max(abs(x[i] - x_old[i]) for i in range(n))
        if diff < tol:
            print(f"Converged in {iteration+1} iterations.")
            return x
    
    print("Did not converge within the maximum number of iterations.")
    return x

A = [
    [10.0, 2.0, 1.0],
    [1.0, 5.0, 1.0],
    [2.0, 3.0, 10.0]
]

b = [9.0, 8.0, 7.0]

solution = gauss_seidel(A, b)
print("Solution:", solution)
