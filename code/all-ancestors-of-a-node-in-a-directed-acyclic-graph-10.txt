class Solution {
public:
    unordered_map<int,vector<int>>graph;
    
    
    
    void dfs(vector<int>&vis,int u,int j,vector<vector<int>>&ans){
        vis[u] = 1;
        for(auto v:graph[u]){
            if(!vis[v]){
                ans[v].push_back(j);
                dfs(vis,v,j,ans);
            }
        }
    }
    
    
    vector<vector<int>> getAncestors(int n, vector<vector<int>>& edges) {
        
        
        for(int i = 0;i<edges.size();i++){
            graph[edges[i][0]].push_back(edges[i][1]);
        }
         
        vector<vector<int>>ans(n);
        for(int i = 0;i<n;i++){
            vector<int>vis(n+1,0);
            dfs(vis,i,i,ans);
        }
        
        
        return ans;
    }
};