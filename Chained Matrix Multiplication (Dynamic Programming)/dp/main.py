# Let p be the array of dimensions, where matrix Ai has dimension p[i-1] x p[i]
def matrix_chain_order(p):
    n = len(p) - 1  # Number of matrices
    m = [[0 for _ in range(n)] for _ in range(n)]  # DP table for minimum costs

    for l in range(2, n+1):
        for i in range(1, n-l+2):
            j = i + l - 1
            m[i-1][j-1] = float('inf')
            for k in range(i, j):
                q = m[i-1][k-1] + m[k][j-1] + p[i-1] * p[k] * p[j]
                if q < m[i-1][j-1]:
                    m[i-1][j-1] = q
                    # Optionally store k to reconstruct solution

    return m[0][n-1]  
