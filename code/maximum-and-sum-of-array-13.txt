class Solution {
public:
    int recur(int idx,vector<int>&nums,vector<int>&wt,int numSlots, map<pair<int,vector<int>>,int>&dp)
    {
        if(idx>=nums.size()) return 0;
        
        if(dp.find({idx,wt})!=dp.end())
            return dp[{idx,wt}];
        int res=INT_MIN;
        for(int k=1;k<=numSlots;k++)
        {
            if(wt[k]<2)
            {
                wt[k]++;
                int ans=(nums[idx] & k) + recur(idx+1,nums,wt,numSlots,dp);
                wt[k]--;
                
                res=max(res,ans);
            }
        }
        return dp[{idx,wt}]=res;
    }
    int maximumANDSum(vector<int>& nums, int numSlots) {
        
        
        vector<int>wt(numSlots+1,0);
        map<pair<int,vector<int>>,int>dp;
        return recur(0,nums,wt,numSlots,dp);
    }
};