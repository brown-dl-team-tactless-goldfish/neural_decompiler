class Solution {
public:
    
    vector<vector<int>>graph;
    vector<int>parent;
    vector<int>subtree;
    vector<int>dist;
    vector<int>value;
    
    // first DFS function will calculate the smallest distance of the current node from the root node.
    
    void dfs1(int u,int p,int lvl){
        parent[u] = p;
        dist[u] = lvl;
        for(int v:graph[u]){
            if(v==p) continue;
            dfs1(v,u,lvl+1);
        }
    }
    
    // Second DFS function calculates the path with maximum amount from the root node to any of the possible leaf nodes.
    
    int dfs2(int u,int p){
        int maxi = -1e9;
        int curr = value[u];
        for(int v:graph[u]){
            if(v==p) continue;
            maxi = max(maxi,dfs2(v,u));
        }
        if(maxi==-1e9) return curr;
        else return curr + maxi;
    }
    
    int mostProfitablePath(vector<vector<int>>& edges, int bob, vector<int>& amount) {
        
        int n = amount.size();
        
        graph.resize(n);
        parent.resize(n,-1);
        subtree.resize(n,0);
        value.resize(n,0);
        dist.resize(n,0);
        
        
        for(int i=0;i<edges.size();i++){
            graph[edges[i][0]].push_back(edges[i][1]);
            graph[edges[i][1]].push_back(edges[i][0]);
        }
        
        dfs1(0,-1,0);
        
        int node = bob;
        int bob_dist = 0;
        
        // Now we need to update the path from the root node to any of the leaf node optimally by cosidering the effect of bob's movement .
        
        while(node!=0){
            
            if(dist[node] > bob_dist) amount[node] = 0;
            else if(dist[node] == bob_dist) amount[node]/=2;
            
            node = parent[node];
            bob_dist++;
            
        }
        
        for(int i=0;i<n;i++){
            value[i] = amount[i];
        }
        
        return dfs2(0,-1);
        
    }
};