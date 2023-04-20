class Solution {
public:
    int dp[100005];
    vector<int> nums;
    int n;
    
    int rec(int level){
        if(level == n){
            return 1;
        }
        if(dp[level] != -1) return dp[level];
        
        bool ok = false;
        
        if(level+1<n){
            if(nums[level] == nums[level+1]) ok|=rec(level+2);
        }
        if(level+2<n){
            if(nums[level] == nums[level+1] && nums[level+1] == nums[level+2]) ok|=rec(level+3);
        }
        if(level+2<n){
            if(nums[level] == nums[level+1]-1 && nums[level+1] == nums[level+2]-1) ok|=rec(level+3);
        }
        
        return dp[level] = ok;
    }
    
    bool validPartition(vector<int>& _nums) {
        nums = _nums;
        n = nums.size();
        memset(dp,-1,sizeof(dp));
        return rec(0);
    }
};