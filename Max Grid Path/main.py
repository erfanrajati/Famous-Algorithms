def transpose(city):
    city_t = [[] for _ in range(len(city[0]))]
    for row in city:
        for i in range(len(row)):
            city_t[i].append(row[i])
    return city_t


n, m = [int(i) for i in input().split()]

city = [[] for _ in range(n)]

for i in range(n):
    populations = [int(p) for p in input().split()]
    city[i].extend(populations)

city_t = transpose(city)

# let dp[i][j] = city_t[i][j] + max(dp[i-1][j+1], dp[i][j+1], dp[i+1][j+1])

def happiness(city_t, dp):
    n = len(city_t)
    m = len(city_t[0])
    # base case
    for i, row in enumerate(city_t[-1]):
        dp[-1][i] = row


    for i in range(n-2, -1, -1):
        for j in range(m):
            # print(f"i={i}\nj={j}")
            mv1 = dp[i+1][j-1] if j else 0
            mv2 = dp[i+1][j]
            mv3 = dp[i+1][j+1] if j != (m-1) else 0
            dp[i][j] = city_t[i][j] + max(mv1, mv2, mv3)
        
        print(i)
        for row in dp:
            print(row)

    
    return max(dp[0])
    # return dp

dp = [
    [0 for _ in city_t[0]]
    for _ in city_t
]

happiness(city_t, dp)
