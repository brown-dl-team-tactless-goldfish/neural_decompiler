class Solution {
public:
    long long maxPoints(vector<vector<int>>& points) {
        int m = points.size();
        int n = points[0].size();
        vector<vector<long long>> dp(m, vector<long long> (n, -1));
        
        for(int j = 0; j < n; j++) {
            dp[0][j] = points[0][j];
        }
        
        for(int i = 1; i < m; i++) {
            vector<long long> left(n, -1);
            vector<long long> right(n, -1);
            
            left[0] = dp[i-1][0] + 0;
            for(int k = 1; k < n; k++) {
                left[k] = max(left[k-1], dp[i-1][k] + k);
            }
            
            right[n-1] = dp[i-1][n-1] - n + 1;
            for(int k = n-2; k >= 0; k--) {
                right[k] = max(right[k+1], dp[i-1][k] - k);
            }
            
            for(int j = 0; j < n; j++) {
                dp[i][j] = max(left[j] - j, right[j] + j) + points[i][j];
            }
        }
        
        long long pts = -1;
        for(int j = 0; j < n; j++) {
            pts = max(pts, dp[m-1][j]);
        }
        
        return pts;
    }
};