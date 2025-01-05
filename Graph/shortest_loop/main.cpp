#include <iostream> 
#include <vector> 
#include <queue>

using namespace std;

int maxn = 1e6;
vector <int> graph[maxn];
int mark[maxn];

void bfs(int src) {
    queue <int> q;
    q.push(src);
    mark[src] = true;
    while ((int)q.size() > 0) {
        int v = q.front();
        q.pop();

        for (int u : graph[v]) {
            if (!mark[u]) {
                q.push(u);
                mark[u] = true;
            }
        }
    }
}


int main() {
    int n, m;
    cin >> n >> m;

    for (int i=0; i<m; ++i) {
        int v, u;
        cin >> v >> u;
        graph[v].push_back(u);
        graph[u].push_back(v);
    }

    for (int v=0; v<n; ++v) {
        bfs(v);
    }

    return 0;
}
