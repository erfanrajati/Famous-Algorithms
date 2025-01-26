# Ice Cream Container Sorting Problem

## Overview

This project addresses the **Ice Cream Container Sorting Problem**, a challenging combinatorial problem involving the reorganization of mixed ice creams in containers under strict constraints. The task is to ensure that each container holds only one type of ice cream while adhering to specific rules.

The problem is tackled using **backtracking**, a systematic search technique that explores all possible configurations and backtracks when a constraint is violated. The project includes two phases, each adding complexity and realism to the problem.

---

## Problem Description

### Phase 1

Given:

- **n containers** with **m** as the maximum capacity (in scoops) for each container.
- Each container initially contains a mixed set of ice creams (e.g., `rgb`, `bgr`).
- Ice cream scoops can only be moved if they are at the top of a container.
- Ice cream scoops can only be placed on a container containing the same type of ice cream or an empty container.

Goal:

- Rearrange the scoops so that each container contains either:
  - One type of ice cream.
  - Or remains empty.

### Phase 2

This phase introduces **variable capacities** for containers and **variable volumes** for ice cream scoops. The constraints are:

1. Containers have specific capacities.
2. Each ice cream type has a volume that may differ due to environmental factors (e.g., heat).
3. Moves must respect the maximum capacity of the containers and the volume constraints.

---

## Solution Approach 

### Phase 1

The first phase solves the simpler version of the problem using:

1. **Validation function**: Ensures that no container exceeds the capacity and that each container has at most one type of ice cream.
2. **Backtracking algorithm**:
   - Explores all possible moves between containers.
   - Backtracks when a move leads to an invalid state.

Steps followed in the code:

- Parse input to initialize containers with their initial ice cream states.
- Define a function to validate the state of all containers.
- Use a backtracking approach to:
  1. Remove the top ice cream from a container.
  2. Attempt placing it in other containers that are either empty or already contain the same type of ice cream, ensuring they do not exceed capacity.
  3. Backtrack if a move results in an invalid state or no solution.
- Record valid moves and return the path leading to a solution.

---

### Phase 2

The second phase expands the problem by incorporating container capacities and ice cream volumes.

1. **Validation function**: Ensures that no container exceeds its capacity and contains only one type of ice cream.
2. **Backtracking algorithm**:
   - Uses an additional parameter for ice cream volumes.
   - Handles variable capacities for containers.
   - Calculates and respects the current volume of each container.

Steps followed in the code:

- Parse input to initialize containers with their capacities and current ice cream states (including volume data).
- Define a function to validate containers based on their capacities and the types of ice creams.
- Use a backtracking approach to:
  1. Remove the top ice cream (along with its volume) from a container.
  2. Attempt placing it in other containers, ensuring capacity constraints are met and only one type of ice cream is allowed per container.
  3. Backtrack if a move violates constraints or leads to a dead end.
- Record and output the sequence of valid moves leading to a solution.

---

## Sample Test Cases

### Test Case 1 (Phase 1):

**Input:**

```
4 3
rr
rgb
bgr
bb
```

**Output:**

```
Solution found!
Moves: [(1, 3), (2, 1), ...]
```

### Test Case 2 (Phase 2):

**Input:**

```
4 3
r 1
g 2
b 3
rr
rgb
bgr
bb
```

**Output:**

```
Solution found!
Moves:
1 4
2 1
...
```

---

## Key Features

1. **Constraint Handling**: Validates container state at every step.
2. **Backtracking Efficiency**: Prunes invalid states to improve performance.
3. **Phase-Specific Logic**: Adapts to evolving problem requirements (e.g., volume constraints).

---

## How to Run

1. Save the code for the desired phase in a Python file.
2. Provide input in the specified format.
3. Observe the output for the solution steps or lack thereof.

---

## Future Work

- Extend the algorithm to handle real-world scenarios (e.g., dynamic input from sensors).
- Optimize the backtracking process with heuristics or Branch and Bound.
- Implement visualization for easier debugging and demonstration.

---

Feel free to reach out for contributions or improvements!

