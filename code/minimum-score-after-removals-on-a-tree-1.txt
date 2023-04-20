class Solution {
    int n;
    vector<vector<int>> adj;
    vector<int> val;
    int LCA[1010][22];
    int level[1000];

    int dfs(vector<int>& A, int u, int par, int lvl = 0) {
        val[u] = A[u];
        level[u] = lvl;
        LCA[u][0] = par;
        for(auto& v : adj[u]) {
            if(v == par) continue;
            val[u] ^= dfs(A, v, u, lvl + 1);
        }
        return val[u];
    }
    void init() {
        for(int j = 0; j < 21; j++) {
            for(int i = 0; i < n; i++) {
                if(LCA[i][j] == -1) continue;
                LCA[i][j+1] = LCA[LCA[i][j]][j];
            }
        }
    }
    int query(int u, int v) {
        if(level[u] < level[v]) swap(u, v);
        int diff = level[u] - level[v];
        for(int i = 0; diff; i++, diff/=2) {
            if(diff&1) u = LCA[u][i];
        }
        if(u != v) {
            for(int i = 21; i >= 0; i--) {
                if(LCA[u][i] == LCA[v][i]) continue;
                u = LCA[u][i];
                v = LCA[v][i];
            }
            u = LCA[u][0];
        }
        return u;
    }
public:
    int minimumScore(vector<int>& A, vector<vector<int>>& edges) {
        n = A.size();
        adj = vector<vector<int>>(n);
        val = vector<int>(n);
        memset(LCA, -1, sizeof LCA);
        memset(level, -1, sizeof level);
        for(auto& e : edges) {
            int u = e[0], v = e[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        dfs(A,0,-1);
        init();
        int res = INT_MAX;
        for(int i = 1; i < n; i++) {
            for(int j = i + 1; j < n; j++) {
                int lca = query(i,j);
                int a, b, c;
                if(lca == i) {
                    a = val[0] ^ val[i], b = val[i] ^ val[j], c = val[j]; 
                } else if(lca == j) {
                    a = val[0] ^ val[j], b = val[j] ^ val[i], c = val[i];
                } else {
                    a = val[0] ^ val[i] ^ val[j], b = val[i], c = val[j];
                }
                int ma = max({a,b,c}), mi = min({a,b,c});
                res = min(res, ma - mi);
            }
        }
        return res;
    }
};