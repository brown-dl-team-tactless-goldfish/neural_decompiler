class DSU
{
    public:
    int findParent(int node,vector<int>& par)
    {
        if(par[node]==node)return node;
        return par[node]=findParent(par[node],par);
    }
    void Union(int u,int v,vector<int> &size,vector<int> &par)
    {
        int pu=findParent(u,par);
        int pv=findParent(v,par);
        if(pu==pv)return;
        if(size[pu]<=size[pv])
        {
            par[pu]=pv;
            size[pv]++;
        }
        else
        {
            par[pv]=pu;
            size[pu]++;
        }
    }
    bool isConnected(int u,int v,vector<int> &par)
    {
        int pu=findParent(u,par);
        int pv=findParent(v,par);
        if(pu==pv)return 1;
        return 0;
    }
};
class Solution {
public:
    vector<bool> friendRequests(int n, vector<vector<int>>& re, vector<vector<int>>& r) {
        DSU dsu;
        vector<int> parent(n,0),size(n,1);
        for(int i=0;i<n;i++)
        {
            parent[i]=i;
        }
        vector<bool> ans;
        for(int i=0;i<r.size();i++)
        {
            int x,y;
            x=dsu.findParent(r[i][0],parent);
            y=dsu.findParent(r[i][1],parent);
            bool ok=true;
            for(int j=0;j<re.size();j++)
            {
                int x1,y1;
                x1=dsu.findParent(re[j][0],parent);
                y1=dsu.findParent(re[j][1],parent);
                if((x==x1&&y==y1)||(x==y1&&y==x1))
                {
                    ok=false;
                    break;
                }
            }
            if(ok)
            {
                dsu.Union(x,y,size,parent);
            }
            ans.push_back(ok);
        }   
        return ans;
    }
};