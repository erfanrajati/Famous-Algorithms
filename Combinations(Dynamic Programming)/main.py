# Recursive
def combinations(n, k, memo=None):
    # Initialize memoization table on the first call
    if memo is None:
        memo = {}

    # Fault case where n < k
    if n < k:
        return 0

    # Base cases
    if k == 0 or k == n:
        return 1

    # Check if the result is already computed
    if (n, k) in memo:
        return memo[(n, k)]

    # Recursive case with memoization
    result = combinations(n - 1, k - 1, memo) + combinations(n - 1, k, memo)
    memo[(n, k)] = result  # Store the result in the memo dictionary
    
    return result


# Non Recursive
def combinations(n, k):
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = 1  # C(i, 0) = 1
        if i <= k:
            dp[i][i] = 1  # C(i, i) = 1
    
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):  # Only compute up to min(i, k) to stay within bounds
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    
    return dp[n][k]


def main():
    n, k = [int(i) for i in input().split()]
    print(combinations(n, k))


if __name__ == "__main__":
    main()



