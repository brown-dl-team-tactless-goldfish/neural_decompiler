class Solution {
public:
    unordered_map<int,vector<int>>  graph;
    unordered_map<int,int> in, out;
    vector<vector<int>> ans;
    stack<int> stk;
    
    void dfs(int u){
        while(out[u]){
            out[u]--;
            int v = graph[u][out[u]];
            dfs(v);
        }
        stk.push(u);
    }
    
    vector<vector<int>> validArrangement(vector<vector<int>>& pairs) {
        unordered_set<int> node;
        for(auto &p : pairs){
            int u=p[0], v=p[1];
            graph[u].push_back(v);
            node.insert(u);
            node.insert(v);
            out[u]++;
            in[v]++;
        }
        
        int start = *node.begin();
        for(auto &u : node){
            if(in[u] < out[u]) start=u;
        }
        
        dfs(start);
        
        int from = stk.top(); stk.pop();
        while(!stk.empty()){
            int to = stk.top(); stk.pop();
            ans.push_back({from,to});
            from=to;
        }
        return ans;
    }
};