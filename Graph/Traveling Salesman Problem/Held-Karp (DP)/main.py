from itertools import *

def held_karp(dist):
    """
    Solves the Traveling Salesman Problem using the Held-Karp dynamic programming algorithm without bitwise operators.

    Parameters:
        dist: 2D list of distances between cities. dist[i][j] gives the distance from city i to city j.

    Returns:
        A tuple (cost, path), where:
            cost: Minimum cost of the TSP tour.
            path: Optimal path that achieves the minimum cost.
    """
    n = len(dist)

    # Create a DP table where dp[mask][i] is the minimum cost to visit all cities in 'mask', ending at city i
    # Instead of using bitmask, we will use a list of subsets
    dp = {}
    parent = {}

    # Base case: cost of starting at city 0 (only city 0 is visited)
    dp[(frozenset([0]), 0)] = 0

    # Iterate over all possible subsets of cities (except the empty set and single city set)
    for size in range(2, n + 1):  # size represents the number of cities in the subset
        for subset in combinations(range(n), size):  # Generate subsets of a given size
            subset_frozen = frozenset(subset)  # Use a frozen set for immutability
            for i in subset:
                if i == 0:
                    continue
                # Find the minimum cost to reach city i from any other city in the subset
                min_cost = float('inf')
                prev_city = -1
                for j in subset:
                    if j == i:
                        continue
                    prev_subset = subset_frozen - frozenset([i])
                    cost = dp.get((prev_subset, j), float('inf')) + dist[j][i]
                    if cost < min_cost:
                        min_cost = cost
                        prev_city = j
                dp[(subset_frozen, i)] = min_cost
                parent[(subset_frozen, i)] = prev_city

    # Reconstruct the minimum cost to complete the tour
    full_subset = frozenset(range(n))  # All cities visited
    min_cost = float('inf')
    last_city = -1
    for i in range(1, n):  # Start from cities other than 0
        cost = dp.get((full_subset, i), float('inf')) + dist[i][0]  # Return to starting city
        if cost < min_cost:
            min_cost = cost
            last_city = i

    # Reconstruct the path
    path = []
    subset = full_subset
    while last_city != -1:
        path.append(last_city)
        prev_city = parent[(subset, last_city)]
        subset = subset - frozenset([last_city])  # Remove last_city from the subset
        last_city = prev_city

    path.append(0)  # Add the starting city to complete the cycle
    path.reverse()

    return min_cost, path


# Example usage
if __name__ == "__main__":
    # Distance matrix
    dist_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    cost, path = held_karp(dist_matrix)
    print("Minimum cost:", cost)
    print("Optimal path:", path)
