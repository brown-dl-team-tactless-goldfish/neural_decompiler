class Solution {
public:
    
    int connectTwoGroups(vector<vector<int>>& cost) {
        int sz1 = cost.size();
        int sz2 = cost[0].size();
        vector<vector<int>> dp(sz1 + 1, vector<int>(1 << sz2, 1e9));
        dp[sz1][(1 << sz2) - 1] = 0;
        for(int i = sz1 - 1; i >= 0; --i) {
            for(int mask = (1 << sz2) - 1; mask >= 0; --mask) {
                for(int j = 0; j < sz2; ++j) {
                    dp[i][mask] = min(dp[i][mask], cost[i][j] + dp[i + 1][mask | (1 << j)]);
                    if(!(mask & (1 << j))) {
                        dp[i][mask] = min(dp[i][mask], cost[i][j] + dp[i][mask | (1 << j)]);
                    }
                }
            }
        }
        return dp[0][0];
    }
};