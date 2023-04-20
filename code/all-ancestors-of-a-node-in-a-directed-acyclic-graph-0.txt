class Solution {
public:
    void dfs(unordered_map<int,vector<int>> &gr,vector<bool> &vis,int src){
        vis[src] = true;
        
        for(auto v:gr[src]){
            if(!vis[v]){
                dfs(gr,vis,v);
            }
        }
    }
    vector<vector<int>> getAncestors(int n, vector<vector<int>>& edges) {
        unordered_map<int,vector<int>>mp;
        
        for(auto i:edges){
            mp[i[1]].push_back(i[0]);
        }
        
        vector<vector<int>>ans;
        
        for(int i=0;i<n;i++){
            
            vector<bool>vis(n,false);
            vector<int>tmp;
            
            dfs(mp,vis,i);
            for(int j=0;j<n;j++){
                if(vis[j] && i!=j){
                    tmp.push_back(j);
                }
            }
            
            ans.push_back(tmp);
        }
        return ans;
    }
};