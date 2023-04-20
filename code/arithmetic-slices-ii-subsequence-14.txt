class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& nums) {
        int ans=0;
        int n=nums.size();
        vector<unordered_map<int,int>>dp(n);
        for(int i=0;i<n;i++){
            for(int j=0;j<i;j++){
                long diff=(long)nums[i]-(long)nums[j];
                if(diff>INT_MAX || diff<INT_MIN)continue;
                dp[i][diff]++;
                if(!dp[j].count(diff))continue;
                dp[i][diff]+=dp[j][diff];
                ans+=dp[j][diff];
            }
        }
        return ans;
    }
};