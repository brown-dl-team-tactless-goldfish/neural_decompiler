class Solution {
public:
    int rsum[100][100], csum[100][100], d1sum[100][100], d2sum[100][100];
    int largestMagicSquare(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                rsum[i][j] = rsum[i][j - 1] + grid[i - 1][j - 1];
                csum[i][j] = csum[i - 1][j] + grid[i - 1][j - 1];
                d1sum[i][j] = d1sum[i - 1][j - 1] + grid[i - 1][j - 1];
                d2sum[i][j] = d2sum[i - 1][j + 1] + grid[i - 1][j - 1];
            }
        }
  
        for(int l = min(m, n); l >= 1; l--) {
            for (int i = 1; i + l - 1 <= m; i++) {
                for (int j = 1; j + l - 1 <= n; j++) {
                    int d1 = d1sum[i + l - 1][j + l - 1] - d1sum[i - 1][j - 1];
                    int d2 = d2sum[i + l - 1][j] - d2sum[i - 1][j + l];                    
                    bool valid = d1 == d2;
                    for (int k = 0; k < l && valid; k++) {
                        valid &= d1 == rsum[i + k][j + l - 1] - rsum[i + k][j - 1];
                        valid &= d1 == csum[i + l - 1][j + k] - csum[i - 1][j + k];
                    }
                    if (valid) return l;
                }
            }
        }
        return 1;
    }
};