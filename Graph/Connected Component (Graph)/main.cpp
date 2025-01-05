#include <iostream>
#include <vector>

using namespace std;

const int maxn = 1e6;  
vector <int> adj[maxn];
bool mark[maxn];
vector <int> vers;

void dfs(int v) {
  vers.push_back(v);
  mark[v] = true;
  for (int u : adj[v])
    if (!mark[u])
      dfs(u);
}

int main() {
  int n, m;
  cin >> n >> m;
  for (int i = 0; i < m; i++) {
    int u, v;
    cin >> u >> v;
    u--, v--;
    adj[u].push_back(v);
    adj[v].push_back(u);
  }

  int cnt = 0;
  for (int v = 0; v < n; v++)
    if (!mark[v]) {
      vers.clear();
      dfs(v);
      cnt++;
      cout << "component: " << cnt << '\n';
      for (int u : vers)
        cout << u + 1 << ' ';
      cout << '\n';
    }
  cout << cnt << endl;

  return 0;
}
