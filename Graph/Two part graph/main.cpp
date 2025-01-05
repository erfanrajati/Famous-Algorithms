#include <iostream>
#include <vector>
 
using namespace std;
 
const int maxn = 1e5;
vector <int> adj[maxn];
bool mark[maxn];
int par[maxn];
int h[maxn];
 
void dfs(int v) {
	mark[v] = true;
	for (int u : adj[v])
		if (!mark[u]) {
			h[u] = h[v] + 1;
			par[u] = v;
			dfs(u);
		} else if (u != par[v]) {
			// back-edge (h[u] < h[v]) or forward-edge (h[u] > h[v])
			if ((h[u] & 1) == (h[v] & 1)) {
				cout << "-1\n";
				exit(0);
			}
		}
}
 
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
 
	int n, m;
	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		int u, v;
		cin >> u >> v;
		u--, v--;
		adj[u].push_back(v);
		adj[v].push_back(u);
	}
 
	for (int v = 0; v < n; v++)
		if (!mark[v]) {
			h[v] = 0;
			par[v] = -1;
			dfs(v);
		}
 
	vector <int> vers[2];
	for (int v = 0; v < n; v++)
		vers[h[v] & 1].push_back(v);
 
	for (int i = 0; i < 2; i++) {
		cout << vers[i].size() << '\n';
		for (int u : vers[i])
			cout << u + 1 << " ";
		cout << '\n';
	}
 
	return 0;
}