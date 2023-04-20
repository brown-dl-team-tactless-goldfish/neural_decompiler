class Solution {
public:
    long long dp[100000][2];
    long long helper(vector<int> &nums  , int i , bool even){
        if(i==(int)nums.size()){
            return 0;
        }
        if(dp[i][even]!=-1) return dp[i][even];
        long long ans = INT_MIN;
        
        ans = max({ans,
                   ((even)?nums[i]:-nums[i]) + helper(nums,i+1,!even),
                   helper(nums,i+1,even)});
        
        return dp[i][even] = ans;
    }
    long long maxAlternatingSum(vector<int>& nums) {
        memset(dp,-1,sizeof(dp));
        long long ans = helper(nums,0,true);
        return ans;
    }
};