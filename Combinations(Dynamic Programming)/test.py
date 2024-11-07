# def combinations(n, k, dp:list[list]):
    
#     pass

# import time
# begin = time.time()
# arr = [
#     [None for i in range(10000)]
#     for _ in range(10000)
# ]
# end = time.time()

# print(format(end - begin, ".3f"))


dp = [[1, 0]]

n = 10
k = 8

def combinations(i, j, n, k, dp):
    if len(dp) == n-1 and len(dp[0]) == k-1:
        return dp[n][k]
    else:
        new_dp = [
            [None for _ in range(j)]
            for _ in range(i)
        ]

        for i in range(len(dp)):
            new_dp[i] = dp[i]

        dp = new_dp

        dp[n][k] = dp[n-1][k-1] + dp[n-1][k]
        return combinations()




print(dp[0][0])