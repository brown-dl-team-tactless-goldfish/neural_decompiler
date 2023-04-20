class Solution {
public:
    int n, vis[1005];

    bool check(vector<int> &stones1 ,vector<int> &stones2) {
        if(stones1[0] == stones2[0] or stones1[1] == stones2[1]) return true;
        return false;
    }

    void dfs(int u, vector<vector<int>>& stones) {
        vis[u] = 1;
        for(int v=0; v<n; v++) {
            if(!vis[v] and check(stones[u], stones[v])) {
                dfs(v, stones);
            }
        }
    }

    int removeStones(vector<vector<int>>& stones) {
        memset(vis, 0, sizeof(vis));
        n = stones.size();

        int cnt = 0;
        for(int u=0; u<n; u++) {
            if(!vis[u]) {
                cnt++;
                dfs(u, stones);
            }
        }

        int ans = n - cnt;
        return ans;
    }
};