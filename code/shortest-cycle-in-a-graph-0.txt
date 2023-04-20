class Solution {
public:
    
    int help(int n,vector<int> adj[]){
        int ans = INT_MAX;
        for (int i = 0; i < n; i++) {
            vector<int> dist(n,(1e9));
            vector<int> par(n, -1);
            dist[i] = 0;
            queue<int> q;
            q.push(i);
            while (!q.empty()) {
                int x = q.front();
                q.pop();
                for (int c : adj[x]) {
                    if (dist[c] == (int)(1e9)) {
                        dist[c] = 1 + dist[x];
                        par[c] = x;
                        q.push(c);
                }
                else if (par[x] != c && par[c] != x)
                    ans = min(ans, dist[x] + dist[c] + 1);
                }
            }
        }
        if (ans == INT_MAX)
            return -1;
        else
            return ans;
    }
    int findShortestCycle(int n, vector<vector<int>>& edges) {
        vector<int> adj[n];
        for(auto i : edges){
            adj[i[0]].push_back(i[1]);
            adj[i[1]].push_back(i[0]);
        }
        return help(n,adj);
    }
};