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

def main():
    n, k = [int(i) for i in input().split()]
    print(combinations(n, k))


if __name__ == "__main__":
    main()