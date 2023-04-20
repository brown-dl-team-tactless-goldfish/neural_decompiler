class Solution {
public:
    
    long long gk, gn, tar;
    int m = 1000000007;
    long long solve(long long count, long long sum, vector<vector<long long>> &dp)
    {
        if(count == gn)
        {
            // cout << sum << endl;
            if(sum == tar) return 1;
            return 0;
        }
        
        if(sum > tar) return 0;
        if(dp[sum][count] != -1) return dp[sum][count];
        
        int c = 0;
        
        for(int i=1; i<=gk; i++)
        {
            c += solve(count+1, sum+i, dp);
            c = c%m;
        }
        
        c = c%m;
        
        return dp[sum][count] = c;
    }
    
    int numRollsToTarget(int n, int k, int target) {
        vector<vector<long long>> dp(target+1, vector<long long>(n+1, -1));
        gk = (long long)(k);
        gn = (long long)(n);
        tar = (long long)(target);
        return solve(0, 0, dp);
    }
};