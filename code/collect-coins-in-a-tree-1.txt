class Solution {
public:
    int collectTheCoins(vector<int>& c, vector<vector<int>>& e) 
    {
        int n = c.size();
        
        vector<set<int>>adj(n+1);
        vector<int>deg(n+1,0);
        for(auto x:e)
        {
            adj[x[0]].insert(x[1]);
            adj[x[1]].insert(x[0]);
            deg[x[0]]++;
            deg[x[1]]++;
        }
        
        vector<int>mark(n+1,0); 
        vector<int>imp(n+1,0);
        queue<int>q;
        
        for(int i=0;i<n;i++)
        {
            if(deg[i]==1)
            {
                q.push(i);
            }
        }
        
        while(!q.empty())
        {
                auto x = q.front();
                q.pop();

                if(deg[x]!=1||imp[x])
                continue;

                deg[x]--;
                auto y = adj[x].begin();
                deg[*y]--;
                
                if(deg[*y]==1)
                q.push(*y);

                if(c[x]) // if leaf node x contains a coin , then the node which x is directly attached with (node *y) will become marked.
                mark[*y]=1;

                if(mark[x]) // if node x is marked,then the node which x is directly attached with (node *y) will become important. 
                imp[*y]=1;

                int va1=x,va2=*y;
                adj[va1].erase(va2);
                adj[va2].erase(va1);
            
           
        }
        
        int ans =0;
        for(int i=0;i<n;i++)
        {
             ans+=deg[i];
        }  
        
        return ans;
        
    }
};