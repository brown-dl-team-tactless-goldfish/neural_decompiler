class Solution {
public:
    long long ans = 0;
    vector<int> graph[100007];
    vector<long long> best;
    long long dfs_sz(int u,int p,vector<int> &pr){
        long long mx = 0;
        for(auto v:graph[u]){
            if(v ==p)continue;
            mx = max(mx,dfs_sz(v,u,pr));
        }
        best[u] = mx;
        return best[u]+pr[u];
    }
    
    void dfs(int u,int p  ,vector<int> &pr){
        vector<pair<long long,int>> A;
        for(auto v:graph[u]){
            A.push_back({best[v]+pr[v],v});
        }
        
        sort(A.rbegin(),A.rend());
        if(A.size())
            ans = max(ans,A[0].first);
        
        for(auto v:graph[u]){
            if(v == p)continue;
            long long last = best[u];
            long long nwBest = 0;
            if(v ==A[0].second && A.size()>1){
                nwBest += A[1].first;
            }
            else if(v != A[0].second){
                nwBest += A[0].first;
            }
            if(p !=-1){
                nwBest = max(nwBest,best[p]);
            }
            
            best[u] = nwBest;
            dfs(v,u,pr);
            
            best[u] = last;
        }
        
    }
    
    long long maxOutput(int n, vector<vector<int>>& edges, vector<int>& price) {
        best.resize(n);
        for(int i = 0;i<n-1;i++){
            int u = edges[i][0];
            int v = edges[i][1];
            graph[u].push_back(v);
            graph[v].push_back(u);
        }
        dfs_sz(0,-1,price);
        dfs(0,-1,price);
        return ans;
    }
};