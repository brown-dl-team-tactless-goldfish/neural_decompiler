class Solution {
public:
    int maximumDetonation(vector<vector<int>>& bombs) {
        int n = bombs.size(), ans = 0;
        unordered_map<int, vector<int>> denote;
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
            {
                int c = within(bombs, i, j);
                if (c == 0)
                {
                    denote[i].push_back(j);
                    denote[j].push_back(i);
                }
                else if (c == 1)
                    denote[i].push_back(j);
                else if (c == 2)
                    denote[j].push_back(i);
            }
        for (int i = 0; i < n; i++)
            ans = max<int>(ans, bfs(denote, i, n));
        return ans;
    }
    
private: 
    int within(vector<vector<int>>& bombs, int i, int j)
    {
        long long dx = bombs[i][0] - bombs[j][0], dy = bombs[i][1] - bombs[j][1], r1 = bombs[i][2], r2 = bombs[j][2];
        long long dist = dx * dx + dy * dy, dr1 = r1 * r1, dr2 = r2 * r2;
        if (dist <= dr1 && dist <= dr2)
            return 0;
        else if (dist <= dr1 && dist > dr2)
            return 1;
        else if (dist > dr1 && dist <= dr2)
            return 2;
        else
            return 3;
    }
    
    int bfs(unordered_map<int, vector<int>>& denote, int i, int& n)
    {
        int ans = 0;
        vector<int> visited(n, 0);
        visited[i] = 1;
        queue<int> q;
        q.push(i);
        while (!q.empty())
        {
            int k = q.front();
            q.pop();
            ans++;
            for (auto& j : denote[k])
                if (visited[j] == 0)
                {
                    visited[j] = 1;
                    q.push(j);
                }
        }
        return ans;
    }
};