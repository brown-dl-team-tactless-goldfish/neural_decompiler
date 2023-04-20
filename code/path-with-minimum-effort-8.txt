class Solution {
public:
    bool inBounds(int r, int c, int n, int m) {
        return r < n && c < m && r >= 0 && c >= 0;
    }

    int minimumEffortPath(vector<vector<int>>& heights) {
        int n = heights.size(), m = heights[0].size();
        vector<vector<int>> efforts(n, vector<int>(m, INT_MAX));

        priority_queue<vector<int>> pq;
        pq.push({0, 0, 0});

        vector<vector<int>> dir = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        while(!pq.empty()) {
            vector<int> min = pq.top(); pq.pop();
            int dist = -min[0], row = min[1], col = min[2];
            if (dist > efforts[row][col]) continue;
            if (row == n - 1 && col == m - 1) return dist;

            for (auto &d : dir) {
                int newRow = row + d[0];
                int newCol = col + d[1];
                if (inBounds(newRow, newCol, n, m)) {
                    int newDist = max(dist, abs(heights[newRow][newCol] - heights[row][col]));
                    if (newDist < efforts[newRow][newCol]) {
                        efforts[newRow][newCol] = newDist;
                        pq.push({-newDist, newRow, newCol});
                    }
                }
            }
        }
        return -1;
    }
};