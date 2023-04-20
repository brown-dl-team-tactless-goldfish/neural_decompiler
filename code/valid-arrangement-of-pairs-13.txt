class Solution {
public:
    unordered_map<int, std::deque<int>> graph;
    unordered_map<int, int> indeg;
    unordered_map<int, int> outdeg;
    set<int> nodes;
    
    vector<vector<int>> validArrangement(vector<vector<int>>& pairs) {
        
        int temp;
        for (auto &pair : pairs)
        {
            graph[pair[0]].push_back(pair[1]);
            
            temp = indeg[pair[0]];
            ++indeg[pair[1]];
            
            temp = outdeg[pair[1]];
            ++outdeg[pair[0]];
            
            nodes.insert(pair[0]);
            nodes.insert(pair[1]);
        }
        
        vector<vector<int>> path;
        path.reserve(pairs.size());
        
        int start = findStart();
        dfs(path, start);
        
        std::reverse(path.begin(), path.end());
        
        return path;
    }
    
private:
    int findStart()
    {
        auto curr = nodes.begin();
        int start = *curr;
        
        for (; curr != nodes.end(); ++curr)
        {
            if (outdeg[*curr] - indeg[*curr] == 1)
                return *curr;
            
            if (outdeg[*curr] > 0)
                start = *curr;
        }
        return start;
    }
    
    
    void dfs(vector<vector<int>> &path, int curr)
    {
        auto &dq = graph[curr];
        while (!dq.empty())
        {
            int n = dq.front();
            dq.pop_front();
            
            dfs(path, n);
            path.push_back({curr, n});
        }
    }
};