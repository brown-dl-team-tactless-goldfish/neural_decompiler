class Solution {
public:
    struct compare{
        bool operator()(pair<int,int> &a, pair<int,int> &b){
            return a.second > b.second;         
        }
    };
    
    vector<int> findAllPeople(int n, vector<vector<int>>& meetings, int firstPerson) {
        vector<vector<pair<int,int>>> graph(n);
        for(auto &g : meetings){
            int u=g[0],v=g[1],t=g[2];
            graph[u].push_back({v,t});
            graph[v].push_back({u,t});
        }
    
        vector<bool> vis(n,false);
        priority_queue<pair<int,int>, vector<pair<int,int>>, compare> q;
        q.push({firstPerson,0});
        q.push({0,0});
		
        while(!q.empty()){
            auto [p,t] = q.top(); q.pop();
			
            if(vis[p]) continue;
            vis[p]=true;
			
            for(auto [newP, newT] : graph[p]){
                if(newT>=t && !vis[newP]){
                    q.push({newP,newT});
                }
            }
        }
        
        vector<int> res;
        for(int i=0; i<n; ++i){
           if(vis[i]) res.push_back(i);
        }
        
        return res;
    }
};