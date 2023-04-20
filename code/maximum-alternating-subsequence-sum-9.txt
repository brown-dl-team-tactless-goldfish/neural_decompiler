#define ll long long int
class Solution {
public:
    ll dp[100003][2];
    long long solve(vector<int> &nums,int idx,int subidx)
    {
        if(idx>=nums.size())
            return 0;
        if(dp[idx][subidx]!=-1)
            return dp[idx][subidx];
        if(subidx)
        {
            return dp[idx][subidx]=max(solve(nums,idx+1,0)-nums[idx],solve(nums,idx+1,1));
        }
        else
        {
            return dp[idx][subidx]=max(nums[idx]+solve(nums,idx+1,1),solve(nums,idx+1,0));
        }
    }
    long long maxAlternatingSum(vector<int>& nums) 
    {
        memset(dp,-1,sizeof(dp));
        return solve(nums,0,0);   
    }
};