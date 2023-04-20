class Solution {
public:
    static bool cmp(vector<int> &a,vector<int> &b)
    {
        return a[2]<b[2];
    }
    
    vector<int> parent;
    
    int find(int x)
    {
        if(parent[x]==x)return x;
        return parent[x] = find(parent[x]);
    }
    
    void Union(int x,int y)
    {
        int lx = find(x);
        int ly = find(y);
        parent[lx] = ly;
    }
    
    vector<bool> distanceLimitedPathsExist(int n, vector<vector<int>>& edges, vector<vector<int>>& q) {
        int m = q.size();
        for(int i = 0;i<m;i++)
        {
            q[i].push_back(i);
        }
        
        parent.resize(n,0);
        for(int i = 0;i<n;i++)
            parent[i] = i;
        sort(edges.begin(),edges.end(),cmp);
        sort(q.begin(),q.end(),cmp);
        
        int i = 0;
        vector<bool> ans(m,0);
        
        for(auto it:q)
        {
            while(i<edges.size() and edges[i][2]<it[2])
            {
                Union(edges[i][0],edges[i][1]);
                i++;
            }
            ans[it[3]] = (find(it[0])==find(it[1]));
        }
        return ans;        
    }
};