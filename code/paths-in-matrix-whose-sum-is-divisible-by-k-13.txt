const int mod = 1e9+7;

class Solution {
public:
    int numberOfPaths(vector<vector<int>>& grid, int k) {
        int m = grid.size();
        int n = grid[0].size();
        
        // 3d dp
        vector<vector<vector<int>>> dp(m, vector<vector<int>>(n, vector<int>(k)));
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(i == 0 && j == 0) {
                    dp[i][j][grid[i][j]%k] += 1;
                } else {
                    for(int l = 0; l < k; l++) {
                        int val = i > 0 ? dp[i-1][j][l] : 0;
                        int val1 = j > 0 ? dp[i][j-1][l] : 0;
                        int rem = (l+grid[i][j])%k;
                        dp[i][j][rem] += (val + val1)%mod;
                        dp[i][j][rem] %= mod;
                    }
                }
            }
        }
        
        return dp[m-1][n-1][0];
    }
};

