class Solution {
public:
    int minSkips(vector<int>& dist, int speed, int hoursBefore) {
        int n = size(dist); 
        vector<vector<long>> dp(n, vector<long>(n, 0)); 
        
        for (int i = 1; i < n; ++i) 
            for (int j = 0; j < n; ++j) {
                dp[i][j] = (dp[i-1][j] + dist[i-1] + speed - 1)/speed*speed; 
                if (j) dp[i][j] = min(dp[i][j], dp[i-1][j-1] + dist[i-1]); 
            }
        
        for (int j = 0; j < n; ++j) {
            if (dp.back()[j] + dist.back() <= (long) speed * hoursBefore) return j; 
        }
        return -1; 
    }
};