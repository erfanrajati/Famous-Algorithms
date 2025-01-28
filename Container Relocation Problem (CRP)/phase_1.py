def is_valid_state(containers):
    # Check if all containers have only one type of ice cream or are empty
    for container in containers:
        if len(container) > 1 and len(set(container)) > 1:
            return False
    return True


def backtrack(containers, visited, path, max_capacity):
    # Base case: check if all containers are valid
    if is_valid_state(containers):
        return path

    # Convert the state into a tuple for visited check
    state = tuple(tuple(container) for container in containers)
    if state in visited:
        return None
    visited.add(state)

    # Try to move the top ice cream from one container to another
    for i in range(len(containers)):
        if not containers[i]:  # Skip empty containers
            continue
        # Remove the top ice cream from the current container
        ice_cream = containers[i].pop()
        for j in range(len(containers)):
            # Skip the same container
            if i == j:
                continue
            # Check if we can place the ice cream in the target container
            if not containers[j] or (containers[j][-1] == ice_cream and len(containers[j]) < max_capacity):
                containers[j].append(ice_cream)
                path.append((i, j))  # Record the move
                result = backtrack(containers, visited, path, max_capacity)
                if result:
                    return result
                # Undo the move (backtrack)
                containers[j].pop()
                path.pop()
        # Undo removing the ice cream
        containers[i].append(ice_cream)

    return None


n, m = [int(i) for i in input().split()]

containers = [[] for _ in range(n)]

for i in range(n):
    container = input()
    containers[i] = list(container)

# Backtracking to solve the problem
visited = set()
path = []  # To record the moves
solution = backtrack(containers, visited, path, m)


# Output the solution
if solution:
    print("Solution found!")
    print("Moves:", solution)
else:
    print("No solution possible.")
