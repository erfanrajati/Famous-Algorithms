# C(n, k) = C(n-1, k-1) + C(n-1, k)

def combinations(n, k):
    # Fault case where k is less than n:
    if n < k:
        return 0

    # Base case where there is only one combination:
    if n == k or k == 0:
        return 1

    # Recursive algorithm:
    return combinations(n-1, k-1) + combinations(n-1, k)

# print(combinations(7, 5))

def main():
    n, k = [int(i) for i in input().split()]
    print(combinations(n, k))


if __name__ == "__main__":
    main()