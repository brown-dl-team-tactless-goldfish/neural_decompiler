class Solution {
public:
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
};
    
    static bool comp(vector<int> &v1,vector<int> &v2)
    {
        return v1[2]<v2[2];        
    }
    vector<vector<int>> findCriticalAndPseudoCriticalEdges(int n, vector<vector<int>>& edges) 
    {
        int len=edges.size();
        for(int i=0;i<len;i++)
            edges[i].push_back(i);
  
        sort(edges.begin(),edges.end(),comp);
 
        DSU dsu;
        int cost=0;
        vector<int> par(n);
        vector<int> size(n,1);
        for(int i=0;i<n;i++)par[i]=i;
        vector<bool> isPart(len,0);
        int c=0;
        for(int i=0;i<len;i++)
        {   
            if(c==n-1)break;
            if(dsu.findParent(edges[i][0],par)!=dsu.findParent(edges[i][1],par))
            {   
                dsu.Union(edges[i][0],edges[i][1],size,par);
                isPart[edges[i][3]]=1;
                cost+=edges[i][2];
                ++c;
            }
        }
        vector<int> critical,pseudocritical;
        for(int i=0;i<len;i++)
        {
            DSU tempDSU;
            vector<int> tempPar(n,0);
            for(int j=0;j<n;j++)tempPar[j]=j;
            
            vector<int> tempSize(n,1);
            int tempCost=0;
            vector<bool> temp(len,0);
            int c=0;
            for(int j=0;j<len;j++)
            {   
                if(c==n-1)break;
                if(j==i)continue;               
                if(tempDSU.findParent(edges[j][0],tempPar)!=tempDSU.findParent(edges[j][1],tempPar))
                {
                    tempDSU.Union(edges[j][0],edges[j][1],tempSize,tempPar);
                    temp[edges[j][3]]=1;
                    tempCost+=edges[j][2];
                    c++;
                }
            }
            if(tempCost==cost)
            {
                for(int k=0;k<len;k++)
                {
                    if(temp[k])isPart[k]=1;
                }    
            }
            else
                critical.push_back(edges[i][3]);
        }
        
        for(int i=0;i<len;i++)
        {
            if(isPart[edges[i][3]])continue;
            DSU tempDSU;
            vector<int> tempPar(n,0);
            for(int j=0;j<n;j++)tempPar[j]=j;
            vector<int> tempSize(n,1);
            int tempCost=0;
            tempDSU.Union(edges[i][0],edges[i][1],tempSize,tempPar);
            tempCost+=edges[i][2];
            int c=0;
            for(int j=0;j<len;j++)
            {  
                if(c==n-1)break;
                if(j==i)continue;               
                if(tempDSU.findParent(edges[j][0],tempPar)!=tempDSU.findParent(edges[j][1],tempPar))
                {
                    tempDSU.Union(edges[j][0],edges[j][1],tempSize,tempPar);
                    tempCost+=edges[j][2];
                    ++c;
                }
            }
            if(tempCost==cost)
                pseudocritical.push_back(edges[i][3]);
        }
        for(auto &it : critical)
            isPart[it]=0;
        for(int i=0;i<len;i++)
        {
            if(isPart[i])
                pseudocritical.push_back(i);
        }
        return {critical,pseudocritical};
    }
};