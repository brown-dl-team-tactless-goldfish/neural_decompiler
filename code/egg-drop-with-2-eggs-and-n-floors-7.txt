class Solution {
public:
     int solve(int k, int n, int dp[3][1001])
    {
        if(k==1 || n==0 || n==1)
        return n;
        if(dp[k][n] != -1)
        return dp[k][n];
        int mn = INT_MAX, low, high;
        for(int k1=1; k1<=n; k1++)
        {
            if(dp[k-1][k1-1] != -1)
            low = dp[k-1][k1-1];
            else
            {
                low = solve(k-1, k1-1, dp);
                dp[k-1][k1-1] = low;
            }
            if(dp[k][n-k1] != -1)
            high = dp[k][n-k1];
            else
            {
                high = solve(k, n-k1, dp);
                dp[k][n-k1] = high;
            }
            int temp = 1 + max(low, high);
            mn = min(mn, temp);
        }
        return dp[k][n] = mn;
    }
    int twoEggDrop(int n) {
        int dp[3][1001];
        memset(dp, -1, sizeof(dp));
        return solve(2, n, dp);
    }
};