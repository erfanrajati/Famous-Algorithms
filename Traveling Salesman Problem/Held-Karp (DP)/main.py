def held_karp(dist):
    """
    Solves the Traveling Salesman Problem using the Held-Karp dynamic programming algorithm.

    Parameters:
        dist: 2D list of distances between cities. dist[i][j] gives the distance from city i to city j.

    Returns:
        A tuple (cost, path), where:
            cost: Minimum cost of the TSP tour.
            path: Optimal path that achieves the minimum cost.
    """
    n = len(dist)

    # Create a DP table where dp[mask][i] is the minimum cost to visit all cities in 'mask', ending at city i
    dp = [[float('inf')] * n for _ in range(1 << n)]
    parent = [[-1] * n for _ in range(1 << n)]  # To reconstruct the path

    # Base case: cost of starting at city 0
    dp[1][0] = 0  # Mask 1 means only city 0 is visited (binary: 0001)

    # Iterate over all subsets of cities (represented as bitmasks)
    for mask in range(1 << n):
        for i in range(n):
            if not (mask & (1 << i)):  # Skip if city i is not in the subset
                continue
            for j in range(n):
                if mask & (1 << j) or j == i:  # Skip if city j is already visited or j == i
                    continue
                new_mask = mask | (1 << j)  # Add city j to the subset
                new_cost = dp[mask][i] + dist[i][j]
                if new_cost < dp[new_mask][j]:
                    dp[new_mask][j] = new_cost
                    parent[new_mask][j] = i

    # Reconstruct the minimum cost to complete the tour
    full_mask = (1 << n) - 1  # All cities visited (binary: 111...1)
    min_cost = float('inf')
    last_city = -1
    for i in range(1, n):  # Start from cities other than 0
        cost = dp[full_mask][i] + dist[i][0]  # Return to starting city
        if cost < min_cost:
            min_cost = cost
            last_city = i

    # Reconstruct the path
    path = []
    mask = full_mask
    while last_city != -1:
        path.append(last_city)
        next_city = parent[mask][last_city]
        mask &= ~(1 << last_city)  # Remove last_city from the subset
        last_city = next_city

    path.append(0)  # Add the starting city to complete the cycle
    path.reverse()

    return min_cost, path


# Example usage
if __name__ == "__main__":
    # Distance matrix
    dist_matrix = [
        [0,  8,  13, 18, 20],
        [3,  0,  7,  8,  10],
        [4,  11, 0,  10, 7 ],
        [6,  6,  7,  0,  1 ],
        [10, 6,  2,  0,  1 ]
    ]

    cost, path = held_karp(dist_matrix)
    print("Minimum cost:", cost)
    print("Optimal path:", path)
