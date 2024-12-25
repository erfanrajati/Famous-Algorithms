seen = []
connected = []


def dfs(graph, vert):
    global seen, connected

    seen.append(vert)
    connected.append(vert)
    for v in graph[vert]:
        if v not in seen:
            dfs(graph, v)


def main():
    global seen, connected

    n, m = [int(i) for i in input().split()]
    graph = {v:[] for v in range(1, n+1)}

    for i in range(m):
        u, v = [int(i) for i in input().split()]
        graph[u].append(v)
        graph[v].append(u)

    for v in graph.keys():
        if v not in seen:
            dfs(graph, v)
            print(len(connected))
            print(*connected, sep=' ')
            connected = []

main()

