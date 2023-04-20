class Solution {
    int mod = 1000000007;
    int dfs(int m, int n, int N, int r, int c,  vector<vector<vector<int>>>& dp) {
        if (r < 0 || c < 0 || r >= m || c >= n) return 1;
        if (N == 0) return 0;
        if (dp[N][r][c] != -1) return dp[N][r][c]%mod;
        
        int moves = 0;
        moves =  (moves + dfs(m, n, N-1, r, c+1, dp))%mod;
        moves =  (moves + dfs(m, n, N-1, r, c-1, dp))%mod;
        moves =  (moves + dfs(m, n, N-1, r+1, c, dp))%mod;
        moves =  (moves + dfs(m, n, N-1, r-1, c, dp))%mod;
        
        dp[N][r][c] = moves%mod;
        return dp[N][r][c];
    }
public:
    int findPaths(int m, int n, int N, int i, int j) {
        vector<vector<vector<int>>>dp(N+1, vector<vector<int>>(m+1, vector<int>(n+1, -1)));
        return dfs(m, n, N, i, j, dp);
    }
};