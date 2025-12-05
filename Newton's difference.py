def forward_difference_table(y_values):
    n = len(y_values)
    table = [[0.0] * n for _ in range(n)]

    for i in range(n):
        table[i][0] = y_values[i]

    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = table[i + 1][j - 1] - table[i][j - 1]

    return table


def backward_difference_table(y_values):
    n = len(y_values)
    table = [[0.0] * n for _ in range(n)]

    for i in range(n):
        table[i][0] = y_values[i]

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            table[i][j] = table[i][j - 1] - table[i - 1][j - 1]

    return table


def divided_difference_table(x_values, y_values):
    n = len(x_values)
    table = [[0.0] * n for _ in range(n)]

    for i in range(n):
        table[i][0] = y_values[i]

    for j in range(1, n):
        for i in range(n - j):
            numerator = table[i + 1][j - 1] - table[i][j - 1]
            denominator = x_values[i + j] - x_values[i]
            table[i][j] = numerator / denominator

    return table


def print_table(header, x_values, table, kind):
    n = len(x_values)
    print(f"\n=== {header} ({kind}) ===")
    cols = ["x", "y"]
    if kind in ("forward", "backward"):
        for j in range(1, n):
            cols.append(f"Δ^{j}y" if kind == "forward" else f"∇^{j}y")
    else:
        for j in range(1, n):
            cols.append(f"f[{j}]")

    print("  ".join(f"{c:>10}" for c in 
    for i in range(n):
        row = [f"{x_values[i]:>10.4f}", f"{table[i][0]:>10.4f}"]
        for j in range(1, n):
            val = table[i][j]
            if (kind in ("forward", "divided") and i > n - j - 1) or \
               (kind == "backward" and i < j):
                row.append(" " * 10)
            else:
                row.append(f"{val:>10.4f}")
        print("  ".join(row))

if __name__ == "__main__":
    x = [0, 1, 2, 3]              
    y = [1, 2, 4, 7]              

    fwd_table = forward_difference_table(y)
    print_table("Forward Difference Table", x, fwd_table, kind="forward")

    bwd_table = backward_difference_table(y)
    print_table("Backward Difference Table", x, bwd_table, kind="backward")

    dd_table = divided_difference_table(x, y)
    print_table("Divided Difference Table", x, dd_table, kind="divided")
