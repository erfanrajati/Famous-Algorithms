import sys

vers = {0:[], 1:[]}
graph = dict()
mark = [0 for _ in range(int(1e5))]
h = [0 for _ in range(int(1e5))]
par = [0 for _ in range(int(1e5))]

def dfs(vert):
    global mark, graph, h, par
    mark[vert] = 1
    for v in graph[vert]:
        if not mark[v]:
            par[v] = vert
            h[v] = h[vert] + 1
            dfs(v)
        elif v != par[vert]:
            # back edge or forward edge
            if h[v] & 1 == h[vert] & 1:
                print(-1)
                sys.exit(0)
        # else: # either the parent or back edge






def main():
    global mark, graph, h, par

    n, m = [int(i) for i in input().split()]


    graph = {v:[] for v in range(n)}

    for i in range(m):
        u, v = [int(i)-1 for i in input().split()]
        graph[u].append(v)
        graph[v].append(u)

    for v in graph.keys():
        if not mark[v]:
            h[v] = 0
            par[v] = -1
            dfs(v)

    for v in graph.keys():
        vers[h[v] & 1].append(v)

    for i in vers.keys():
        for v in vers[i]:
            print(v+1, end=' ')
        print()


    
main()