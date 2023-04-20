class Solution {
    void dfs(int node, vector<int> adj[], vector<int> &vis, int &mn) {
        vis[node] = 1;
        mn = min(mn, node);
        for(int ad : adj[node]) {
            if(!vis[ad]) dfs(ad, adj, vis, mn);
        }
    }
public:
    string smallestEquivalentString(string s1, string s2, string baseStr) {
        int n = s1.size();
        vector<int> adj[26];
        for(int i=0; i<n; i++) {
            adj[s1[i] - 'a'].push_back(s2[i] - 'a');
            adj[s2[i] - 'a'].push_back(s1[i] - 'a');
        }

        vector<int> sol(26);
        for(char c='a'; c<='z'; c++) {
            vector<int> vis(26);
            int mn = 27;
            dfs(c - 'a', adj, vis, mn);
            sol[c - 'a'] = mn;
        }
        
        string ans;
        for(char c : baseStr) ans += sol[c - 'a'] + 'a';
        
        return ans;
    }
};