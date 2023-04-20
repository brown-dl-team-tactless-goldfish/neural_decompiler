class Solution {
    void dfs(int node, vector<pair<int, int>> adj[], vector<int> &vis, int &ans) {
        vis[node] = 1;
        for(auto ad : adj[node]) {
            ans = min(ans, ad.second);
            if(!vis[ad.first]) dfs(ad.first, adj, vis, ans);
        }
    }
public:
    int minScore(int n, vector<vector<int>>& roads) {
        vector<pair<int, int>> adj[n + 1];
        for(auto e : roads) adj[e[0]].push_back({e[1], e[2]}), adj[e[1]].push_back({e[0], e[2]});
        
        int ans = 1e9;
        vector<int> vis(n + 1);
        dfs(n, adj, vis, ans);
        return ans;
    }
};