class Solution {
public:
    int kInversePairs(int n, int k) {        
        // dp[i][m]:the number of different arrays consist of numbers from 1 to i such that there are exactly k inverse pairs
        // dp[n][k]:the anwser we are looking for
        //vector<vector<int>> dp(n + 1, vector<int>(k + 1, 0));  // Okay
        int dp[1001][1001]={};
        dp[0][0]=1;
        const int M = 1e9+7;
        for(int i = 1; i <= n; i++)
            for(int j = 0; j <= k; j++)
                for(int m = 0; m < i; m++)
                    if(j-m >=0 && j-m <= k)
                        dp[i][j] = (dp[i][j] + dp[i-1][j-m])%M;
        return dp[n][k];
    }
};