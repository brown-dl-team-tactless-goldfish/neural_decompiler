class Solution {
public:
    vector<vector<int>> ans;
    void DFS(vector<vector<int>>& Graph, vector<int>& disc, vector<int>& low, vector<bool>& visited, int node, int time, int parent) {
        visited[node] = true;
        low[node] = disc[node] = ++time;
        for(int edge : Graph[node]) {
            if(edge == parent) continue;
            if(! visited[edge]) {
                DFS(Graph, disc, low, visited, edge, time, node);
                low[node] = min(low[node], low[edge]);
                if(low[edge] > disc[node]) ans.push_back({node, edge});
            } else low[node] = min(low[node], low[edge]);
        }
    }
    
    vector<vector<int>> criticalConnections(int n, vector<vector<int>>& connections) {
        vector<int> disc(n, INT_MIN), low(n, INT_MIN);
        vector<bool> visited(n, false);
        //make graph
        vector<vector<int>> Graph(n);
        for(auto it : connections) {
            Graph[it[0]].push_back(it[1]);
            Graph[it[1]].push_back(it[0]);
        }
        
        for(int i = 0; i < n; i++) {
            if(! visited[i]) DFS(Graph, disc, low, visited, i, 0, -1); // time, parent
        }
        return ans;
    }
};