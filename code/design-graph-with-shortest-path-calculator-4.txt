class Graph {
    int n;
    unordered_map<int, vector<pair<int, int>>> adj;
public:
    Graph(int m, vector<vector<int>>& edges) {
        for(auto e : edges) adj[e[0]].push_back({e[1], e[2]});
        n = m;
    }
    
    void addEdge(vector<int> e) {
        adj[e[0]].push_back({e[1], e[2]});
        n++;
    }
    
    int shortestPath(int a, int b) {
        vector<int> d(n, 1e9);
        d[a] = 0;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        pq.push({0, a});
        
        while(pq.size()) {
            int dis = pq.top().first, node = pq.top().second;
            pq.pop();
            if(node == b) return dis;
            
            for(auto ad : adj[node]) {
                if(dis + ad.second < d[ad.first]) {
                    d[ad.first] = dis + ad.second;
                    pq.push({d[ad.first], ad.first});
                }
            }
        }
        return -1;
    }
};

/**
 * Your Graph object will be instantiated and called as such:
 * Graph* obj = new Graph(n, edges);
 * obj->addEdge(edge);
 * int param_2 = obj->shortestPath(node1,node2);
 */