class Solution {
public:
    int reachableNodes(int n, vector<vector<int>>& edges, vector<int>& restricted) {
        vector<int> graph[n];
        for(vector<int> &edge : edges)
        {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }
        vector<bool> visited;
        for(int i = 0; i < n; i++)
            visited.push_back(0);
        for(int i = 0; i < restricted.size(); i++)
            visited[restricted[i]] = 1;
        queue<int> q;
        q.push(0);
        int ans = 0;
        if(visited[0])
            return ans;
        visited[0] = 1;
        while(!q.empty())
        {
            int sz = q.size();
            while(sz--)
            {
                int val = q.front();
                q.pop();
                ans++;
                for(int &node : graph[val])
                {
                    if(visited[node])
                        continue;
                    q.push(node);
                    visited[node] = 1;
                }
            }
        }
        return ans;
    }
};