class Solution {
public:
    vector<int>par,sz;
    vector<pair<int, pair< pair<int,int>, pair<int,int>>>> edges;
    
    //DSU Section
    int root(int u){
        return u==par[u]?u:par[u] = root(par[u]);
    }
    void join(int u,int v){
        u = root(u);
        v = root(v);
        if(u==v)return;
        par[u] = v;
        sz[v]+=sz[u];
    }
    
    
    vector<int> maxPoints(vector<vector<int>>& grid, vector<int>& queries) {
        int q = queries.size();
        vector<int>qord(q);
        iota(qord.begin(),qord.end(),0);
        // Order the queries.
        sort(qord.begin(),qord.end(),[&queries](int x,int y){
            return queries[x]<queries[y];
        });
        
        int n = grid.size();
        int m = grid[0].size();
        const int fx[4]={0,0,1,-1};
        const int fy[4]={1,-1,0,0};
        edges.clear();
        //Find all the edges.
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                for(int k=0;k<4;k++){
                    int di = i+fx[k];
                    int dj = j+fy[k];
                    if(di>=0 && di<n && dj>=0 && dj<m){
                        edges.push_back({max(grid[di][dj],grid[i][j]),{{i,j},{di,dj}}});
                    }
                }
            }
        }
        
        //Sort all the edges.
        sort(edges.begin(),edges.end());
        par.resize(m*n);
        iota(par.begin(),par.end(),0);
        sz.resize(m*n);
        for(int i=0;i<m*n;i++)sz[i] = 1;
        int ql = 0;
        vector<int>ans(q);
        //Queries with value less than grid[0][0] will have answer equal to 0.
        while(ql<q && queries[qord[ql]]<=grid[0][0]){
            ans[qord[ql]] = 0;
            ql++;
        }
        //Start processing the edges.
        for(auto&e:edges){
            int cost = e.first;
            int u = e.second.first.first*m+e.second.first.second;
            int v = e.second.second.first*m+e.second.second.second;
            while(ql<q && queries[qord[ql]]<=cost){
                ans[qord[ql]] = sz[root(0)];
                ql++;
            }
            join(u,v);
            
        }
        //Remaining Queries will have answer equal to grid size.
        while(ql<q){
            ans[qord[ql]] = sz[root(0)];
            ql++;
        }
        return ans;
    }
};