# Matrix Chain Multiplication using Dynamic Programming

def matrix_chain_order(p):
    n = len(p) - 1

    # dp[i][j] stores minimum scalar multiplications
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # length is chain length
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float("inf")

            for k in range(i, j):
                cost = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + p[i] * p[k + 1] * p[j + 1]
                )

                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp


print("=" * 60)
print("MATRIX CHAIN MULTIPLICATION")
print("USING DYNAMIC PROGRAMMING")
print("=" * 60)

n = int(input("Enter number of matrices: "))

dimensions = []

print("\nEnter dimensions:")
for i in range(n):
    rows = int(input(f"Enter rows of Matrix {i + 1}: "))
    cols = int(input(f"Enter columns of Matrix {i + 1}: "))

    if i > 0 and rows != dimensions[-1]:
        print("Invalid dimensions! Matrix multiplication is not possible.")
        exit()

    dimensions.append(rows)
    dimensions.append(cols)

# Remove duplicate middle dimensions
p = [dimensions[0]]
for i in range(1, len(dimensions), 2):
    p.append(dimensions[i])

dp = matrix_chain_order(p)

print("\nMinimum number of scalar multiplications:",
      dp[0][n - 1])

print("\nTime Complexity: O(n^3)")
print("Space Complexity: O(n^2)")

print("=" * 60)