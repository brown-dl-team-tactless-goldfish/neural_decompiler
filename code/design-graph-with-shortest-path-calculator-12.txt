class Graph
{
public:
    unordered_map<int, vector<pair<int, int>>> graph;
    int k;
    Graph(int n, vector<vector<int>> &e)
    {
        for (auto x : e)
        {
            vector<int> l;
            graph[x[0]].push_back({x[1], x[2]});
        }
        k = n;
    }
    void addEdge(vector<int> e)
    {
        graph[e[0]].push_back({e[1], e[2]});
    }
    int shortestPath(int n1, int n2)
    {
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> p;
        p.push({0, n1});
        vector<int> dis(k + 1, 1e9);
        dis[n1] = 0;
        while (!p.empty())
        {
            int dist = p.top().first;
            int node = p.top().second;
            p.pop();
            for (auto i : graph[node])
            {
                if (dist + i.second < dis[i.first])
                {
                    dis[i.first] = dist + i.second;
                    p.push({dis[i.first], i.first});
                }
            }
        }
        if (dis[n2] == 1e9)
            return -1;
        else
            return dis[n2];
    }
};

/**
 * Your Graph object will be instantiated and called as such:
 * Graph* obj = new Graph(n, edges);
 * obj->addEdge(edge);
 * int param_2 = obj->shortestPath(node1,node2);
 */