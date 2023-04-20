class Solution {
    int dfs(int i, int j, vector<vector<int>> &dp, vector<int>& nums, vector<int>& mul, int m)
    {
        if(m >= mul.size())
            return 0;
        if(dp[i][j] != INT_MIN)
            return dp[i][j];
        int idx = nums.size()-j-1;
        int l = nums[idx]*mul[m] + dfs(i, j+1, dp, nums, mul, m+1);
        int r = nums[i]*mul[m] + dfs(i+1, j, dp, nums, mul, m+1);
        return dp[i][j] = max(l,r);
    }
public:
    int maximumScore(vector<int>& nums, vector<int>& mul) {
        int n = nums.size(), m = mul.size();
        vector<vector<int>> dp(m+1, vector<int> (m+1, INT_MIN));
        return dfs(0,0, dp, nums, mul, 0);
    }
};