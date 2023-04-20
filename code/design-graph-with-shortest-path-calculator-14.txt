class Graph {
public:
    vector<pair<int,int>> v[101];
    typedef pair<int,int> pi;
    Graph(int n, vector<vector<int>>& edges) {
        for(auto it:edges)
        {
            v[it[0]].push_back({it[1],it[2]});
        }
    }
    
    void addEdge(vector<int> edge) {
         v[edge[0]].push_back({edge[1],edge[2]});
    }
    
    int shortestPath(int node1, int node2) {
        vector<int> dist(101,INT_MAX);
        dist[node1]=0;
        priority_queue<pi,vector<pi>,greater<pi>> pq;
        pq.push({dist[node1],node1});
        while(!pq.empty())
        {
            int val=pq.top().first;
            int node=pq.top().second;
            pq.pop();
            for(auto it:v[node])
            {
                int x=it.first;
                int wt=it.second;
                if(dist[x]>dist[node]+wt)
                {
                    dist[x]=dist[node]+wt;
                    pq.push({dist[x],x});
                }
            }
        }
        return (dist[node2]==INT_MAX)?-1:dist[node2];
    }
};

/**
 * Your Graph object will be instantiated and called as such:
 * Graph* obj = new Graph(n, edges);
 * obj->addEdge(edge);
 * int param_2 = obj->shortestPath(node1,node2);
 */