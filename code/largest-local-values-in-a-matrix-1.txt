class Solution {
public:
    vector<vector<int>> largestLocal(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<vector<int>> ans(n - 2, vector<int>(n - 2, 0));
        for (int r = 1; r < n - 1; r++) {
            for (int c = 1; c < n - 1; c++) {
                ans[r - 1][c - 1] = maxLocal(grid, r, c);
            }
        }
        return ans;
    }

private:
    int maxLocal(vector<vector<int>>& grid, int r, int c) {
        int mx = INT_MIN;
        for (int i = r - 1; i <= r + 1; i++) {
            for (int j = c - 1; j <= c + 1; j++) {
                mx = max(mx, grid[i][j]);
            }
        }
        return mx;
    }
};