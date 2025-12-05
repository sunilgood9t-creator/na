def gauss_elimination_pivot(A, b):
    n = len(A)
    M = [A[i][:] + [b[i]] for i in range(n)]

    for k in range(n):
        max_row = max(range(k, n), key=lambda i: abs(M[i][k]))
        if abs(M[max_row][k]) < 1e-12:
            raise ValueError("Matrix is singular or nearly singular.")

        if max_row != k:
            M[k], M[max_row] = M[max_row], M[k]

        for i in range(k + 1, n):
            factor = M[i][k] / M[k][k]
            for j in range(k, n + 1):
                M[i][j] -= factor * M[k][j]

    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        if abs(M[i][i]) < 1e-12:
            raise ValueError("Matrix is singular or nearly singular (during back-substitution).")

        s = sum(M[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (M[i][n] - s) / M[i][i]

    return x


if __name__ == "__main__":
    A = [
        [2.0,  1.0, -1.0],
        [-3.0, -1.0, 2.0],
        [-2.0,  1.0, 2.0]
    ]
    b = [8.0, -11.0, -3.0]

    sol = gauss_elimination_pivot(A, b)
    print("Solution:", sol)
