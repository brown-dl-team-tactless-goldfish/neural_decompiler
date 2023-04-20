typedef pair<int, int> pii;

class Solution {
private:
    vector<vector<int>> graph;
    priority_queue<pii, vector<pii>, greater<pii>> min_heap;
    
public:
    int secondMinimum(int n, vector<vector<int>>& edges, int time, int change) {
        graph.resize(n+1);
        
        for(auto it: edges) {
            int u = it[0];
            int v = it[1];
            graph[u].push_back(v);
            graph[v].push_back(u);
        }
        
        // for visiting each node at most 2 times
        vector<int> freq(n+1, 0);
        vector<int> weight(n+1, INT_MAX);
        
        
        // {time, node}
        min_heap.push({0, 1});
        weight[1] = 0;
        
        int cnt = 0;
        while(!min_heap.empty()) {
            auto curr = min_heap.top();
            min_heap.pop();
            int w = curr.first;
            int u = curr.second;
            
            freq[u] += 1;
            
            int elapse = w / change;
            if(elapse%2) 
                w += (change * (elapse+1)) - w;
        
            for(int v: graph[u]) {
                if(w + time != weight[v] && freq[v] <= 2) {
                    weight[v] = w + time;
                    if(v == n) {
                        cnt += 1;
                        if(cnt == 2)
                            return weight[v];
                    }  
                    min_heap.push({weight[v], v});
                }
            }
            
        }
        
        return 0;
    }
};
