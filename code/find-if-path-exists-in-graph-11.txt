class Solution {
public:
    vector<int> g[200005];
    int vis[200005];
    void dfs(int u) {
        vis[u] = 1;
        for(auto v: g[u]) {
            if(!vis[v]) {
                dfs(v);
            }
        }
    }
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        for(auto x: edges) {
            g[x[0]].push_back(x[1]);
            g[x[1]].push_back(x[0]);
        }
        dfs(source);
        if(vis[destination]) return true;
        else return false;
    }
};