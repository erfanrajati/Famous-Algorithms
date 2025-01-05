d = [45, 11, 22, 25, 1, 4, 2, 31] # list of all matrix dimensions

costs = []
total_cost = 0
while len(d) > 3:
    for i in range(len(d[:-2])):
        cost = d[i] * d[i+1] * d[i+2]
        costs.append(cost)

    temp = min(costs)
    total_cost += temp
    target = costs.index(temp)
    d.pop(target+1)
    costs = []

print(total_cost + (d[0] * d[1] * d[2]))