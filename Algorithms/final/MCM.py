def matrix_chain_order(dimensions):
    """
    Computes the optimal parenthesization of a matrix chain product
    and the minimum number of scalar multiplications needed.

    Parameters:
    dimensions (list): List of dimensions of matrices such that
                       the ith matrix has dimensions dimensions[i-1] x dimensions[i].

    Returns:
    tuple: A tuple containing the following:
           - Minimum number of scalar multiplications.
           - Table of costs (m).
           - Table for optimal splits (s).
    """
    n = len(dimensions) - 1  # Number of matrices
    # m[i][j] will store the minimum number of scalar multiplications for A_i..A_j
    m = [[0] * n for _ in range(n)]
    # s[i][j] will store the index k at which the optimal split occurs
    s = [[0] * n for _ in range(n)]

    # L is chain length
    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            m[i][j] = float('inf')  # Initialize with infinity
            for k in range(i, j):
                # Compute cost
                q = m[i][k] + m[k + 1][j] + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m[0][n - 1], m, s


def print_optimal_parenthesization(s, i, j):
    """
    Prints the optimal parenthesization of matrices.

    Parameters:
    s (list): The table for optimal splits.
    i (int): Starting index.
    j (int): Ending index.
    """
    if i == j:
        print(f"A{i + 1}", end="")
    else:
        print("(", end="")
        print_optimal_parenthesization(s, i, s[i][j])
        print_optimal_parenthesization(s, s[i][j] + 1, j)
        print(")", end="")


# Example usage
if __name__ == "__main__":
    print("""Input: The dimensions list specifies the dimensions of the matrices. For instance, if dimensions = [30, 35, 15], the matrices are:
    A1 : 30 x 35
    A2 : 35 x 15
    """)
    dimensions = [int(i) for i in input("Enter the space separated dimensions matrix - ").split()]
    min_cost, m, s = matrix_chain_order(dimensions)
    print(f"Minimum number of multiplications: {min_cost}")
    print("Optimal parenthesization: ", end="")
    print_optimal_parenthesization(s, 0, len(dimensions) - 2)
    print()
