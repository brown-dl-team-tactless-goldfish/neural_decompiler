class Solution {
    void dfs(int node, vector<int> adj[], vector<int> &removed) {
        removed[node] = 1;
        for(int ad : adj[node]) {
            if(!removed[ad]) dfs(ad, adj, removed);
        }
    }
public:
    int removeStones(vector<vector<int>>& stones) {
        int n = stones.size();
        vector<int> adj[n];

        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) {
                if(i != j && (stones[i][0] == stones[j][0] || stones[i][1] == stones[j][1])) adj[i].push_back(j);
            }
        }
        
        vector<int> removed(n, 0);
        int ans = n;
        for(int i=0; i<n; i++) {
            if(!removed[i]) dfs(i, adj, removed), ans--;
        }

        return ans;
    }
};
