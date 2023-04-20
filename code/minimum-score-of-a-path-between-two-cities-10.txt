class Solution {
public:
    void dfs(int node,vector<int> &vis,vector<pair<int,int>> adj[],int &ans){
        vis[node] = 1;
        for(auto x : adj[node]){
            ans = min(ans,x.second);
        }
        for(auto x : adj[node]){
            if(vis[x.first]==0){
                dfs(x.first,vis,adj,ans);
            }
        }
    }
    int minScore(int n, vector<vector<int>>& roads) {
        vector<pair<int,int>> adj[n+1];
        for(auto it : roads){
            adj[it[0]].push_back({it[1],it[2]});
            adj[it[1]].push_back({it[0],it[2]});
        }
        vector<int> vis(n+1,0);
        int ans=INT_MAX;
        dfs(1,vis,adj,ans);
        if(vis[1]==1 && vis[n]==1) {return ans;}
        return 0;
    }
};