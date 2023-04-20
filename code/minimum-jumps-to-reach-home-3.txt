class Solution {
    unordered_map<int, int> um;
    int dfs(int a, int b, int x, int val, int pn, vector<vector<int>> &dp)
    {
        if(val == x) return 0;
        if(um.count(val)) return 6000;
        if(val < 0 || val > 6000) return 6000;
        if(dp[val][pn] != -1)
            return dp[val][pn];
        dp[val][pn] = 1 + dfs(a,b,x,val+a, 0, dp);
        if(pn == 0)
            dp[val][pn] = min(dp[val][pn], 1+dfs(a, b, x, val-b, 1,dp));
        return dp[val][pn];
    }
public:
    int minimumJumps(vector<int>& forbidden, int a, int b, int x) {
        vector<vector<int>> dp(6001, vector<int> (2, -1));
        for(int &num : forbidden)
        {
            if(num == x) return -1;
            um[num]++;
        }
        int val = dfs(a, b, x, 0, 0, dp);
        if(val >= 6000) return -1;
        return val;
    }
};