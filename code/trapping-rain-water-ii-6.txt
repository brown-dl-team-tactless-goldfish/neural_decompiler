class Solution {
public:
    priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> pq;
    int n, m, result = 0;
    vector<int> DIR = {1, 0, -1, 0, 1};
    int trapRainWater(vector<vector<int>>& h) {
        n = h.size(), m = h[0].size();
        vector<vector<bool>> vis(n, vector<bool>(m));
        for(int i = 0; i < n; i++)
            for(int j = 0; j < m; j++)
                if(!i || !j || i == n - 1 || j == m - 1)
                    pq.push({h[i][j], {i, j}}), vis[i][j] = true;
        int maxN = -2e8;
        while(!pq.empty()){
            auto cost = pq.top().first;
            auto [r, c] = pq.top().second;
            pq.pop();
            maxN = max(maxN, h[r][c]);
            for(int k = 0; k < 4; k++){
                int nr = r + DIR[k], nc = c + DIR[k + 1];
                if(nr < 0 || nc < 0 || nr == n || nc == m || vis[nr][nc]) continue;
                vis[nr][nc] = true;
                result += max(0, maxN - h[nr][nc]);
                pq.push({h[nr][nc], {nr, nc}});
            }
        }
        return result;
    }
};