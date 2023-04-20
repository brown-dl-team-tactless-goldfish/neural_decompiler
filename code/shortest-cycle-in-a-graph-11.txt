class Solution {
public:
   int findShortestCycle(int n, vector<vector<int>>& edges) {
    vector<vector<int>> adj(n);
    for (auto& e : edges) {
        adj[e[0]].push_back(e[1]);
        adj[e[1]].push_back(e[0]);
    }
    int min_cycle = n + 1;
    for (int i = 0; i < n; i++) {
        vector<int> dist(n, -1);
        dist[i] = 0;
        queue<int> q;
        q.push(i);
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (int v : adj[u]) {
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    q.push(v);
                } else if (dist[v] >= dist[u]) {
                    min_cycle = min(min_cycle, dist[v] + dist[u] + 1);
                }
            }
        }
    }
    return min_cycle <= n ? min_cycle : -1;
}

};