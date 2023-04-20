class Solution {
private:
    typedef pair<int, pair<int, int>> pi;
public:
    int swimInWater(vector<vector<int>>& grid) {
        int n = grid.size();
        set<pair<int, int>> visit;        
        priority_queue<pi, vector<pi>, greater<pi>> pq;
        pq.push({grid[0][0], {0, 0}});
        visit.insert({0, 0});
        
        vector<vector<int>> dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        
        while (!pq.empty())
        {
            int t = pq.top().first, r = pq.top().second.first, c = pq.top().second.second; pq.pop();
            if (r == n - 1 && c == n - 1)
            {
                return t;
            }
            for (const auto& d : dirs)
            {
                int i = r + d[0], j = c + d[1];
                if (i < 0 || j < 0 || i >= n || j >= n || (visit.find({i, j}) != visit.end()))
                {
                    continue;
                }
                visit.insert({i, j});
                pq.push({max(t, grid[i][j]), {i, j}});                    
            }
        }
        return 0;
    }
};