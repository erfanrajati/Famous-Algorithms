def is_valid_state(containers):
    """
    Check if all containers are valid.
    A container is valid if it does not exceed its capacity and contains only one type of ice cream.
    """
    for capacity, container in containers:
        if len(container) > 1 and len(set(ice for ice, _ in container)) > 1:
            return False
        if sum(vol for _, vol in container) > capacity:
            return False
    return True


def backtrack(containers, visited, path, ice_creams):
    """
    Backtracking function to rearrange ice creams.
    """
    # Base case: check if all containers are valid
    if is_valid_state(containers):
        return path

    # Convert the state into a tuple for visited check
    state = tuple((cap, tuple(container)) for cap, container in containers)
    if state in visited:
        return None
    visited.add(state)

    # Try to move the top ice cream from one container to another
    for i in range(len(containers)):
        _, source_container = containers[i]
        if not source_container:  # Skip empty containers
            continue
        # Remove the top ice cream from the current container
        ice_cream, volume = source_container.pop()
        for j in range(len(containers)):
            if i == j:
                continue  # Skip the same container
            target_capacity, target_container = containers[j]
            # Calculate the current volume of the target container
            current_volume = sum(vol for _, vol in target_container)
            # Check if we can place the ice cream in the target container
            if (not target_container or target_container[-1][0] == ice_cream) and (current_volume + volume <= target_capacity):
                target_container.append((ice_cream, volume))
                path.append((i, j))  # Record the move
                result = backtrack(containers, visited, path, ice_creams)
                if result:
                    return result
                # Undo the move (backtrack)
                target_container.pop()
                path.pop()
        # Undo removing the ice cream
        source_container.append((ice_cream, volume))

    return None



# Example input
# containers = [
#     list("rgb"),  # Container 1
#     list("bgr"),  # Container 2
#     list("rr"),   # Container 3
#     list("bb")    # Container 4
# ]

n, c = [int(i) for i in input().split()]

ice_creams = dict()
for _ in range(c):
    k, v = input().split()
    ice_creams[k] = int(v)

containers = [[1, []] for _ in range(n+1)]

for i in range(n):
    temp = input().strip()
    container = [(c,ice_creams[c]) for c in temp]
    if temp:
        h = max(map(lambda item:item[1], container))
        containers[i][0] = len(container) + h # Set the capacity of each container
        containers[i][1] = container


# Backtracking to solve the problem
visited = set()
path = []  # To record the moves
solution = backtrack(containers, visited, path, ice_creams)


# Output the solution
if solution:
    print("Solution found!")
    print("Moves:")
    for init, fin in solution:
        print(init, fin)
else:
    print("No solution possible.")
