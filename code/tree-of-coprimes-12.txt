class Solution {
public:
    vector<vector<int>>adj;
    vector<int>res,val;
    void dfs(int u,int h,int prev,vector<int>anc,vector<int>pos)
    {
        int ans=-1,p=-1;
        for(int i=1;i<=50;i++)
        {
            if(anc[i]!=-1 && __gcd(i,val[u])==1)
            {
                if(pos[i]>p)
                {
                    ans=anc[i];
                    p=pos[i];
                }
            }
        }
        res[u]=ans;
        anc[val[u]]=u;
        pos[val[u]]=h;
        for(auto &v:adj[u])
        {
            if(v==prev)
                continue;
            dfs(v,h+1,u,anc,pos);
        }
    }
    vector<int> getCoprimes(vector<int>& nums, vector<vector<int>>& edges) 
    {
        val=nums;
        int n=nums.size();
        adj.resize(n);
        res.resize(n,-1);
        for(auto &v:edges)
        {
            adj[v[0]].push_back(v[1]);
            adj[v[1]].push_back(v[0]);
        }
        vector<int>pos(51,-1),anc(51,-1);
        dfs(0,0,-1,anc,pos);
        return res;
    }
};